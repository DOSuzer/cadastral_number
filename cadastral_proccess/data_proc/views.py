from celery.result import AsyncResult
from django.db import connection
from django.shortcuts import get_object_or_404
from rest_framework import status, views
from rest_framework.response import Response

from .models import CadastralData
from .pagination import MyPaginationClass
from .serializers import DataSerializer, HistorySerializer, ResultSerializer
from .tasks import send_request


class QueryView(views.APIView):
    """Принимает запрос с кадастровыми данными."""

    def post(self, request, format=None):
        """POST запрос с данными."""
        serializer = DataSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        obj = serializer.save()
        task = send_request.delay(serializer.data, obj.id)
        return Response(
            {'status': 'Запрос отправлен.',
             'record_id': obj.id,
             'task_id': task.task_id},
            status=status.HTTP_200_OK,
        )


class ResultView(views.APIView):
    """Отправляет результаты запроса."""

    def get(self, request, format=None):
        """GET запрос результатов."""
        serializer = ResultSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        obj = get_object_or_404(CadastralData,
                                id=serializer.validated_data['record_id'])
        res = AsyncResult(serializer.validated_data['task_id'])
        return Response(
            {'status': res.state, 'result': obj.result},
            status=status.HTTP_200_OK,
        )


class PingView(views.APIView):
    """Отправляет состояние сервера."""

    def get(self, request, format=None):
        """GET запрос состояния сервера."""
        server_status = {
            'status': 'Сервер работает',
            'database': connection.vendor
        }
        return Response(server_status, status=status.HTTP_200_OK)


class HistoryView(views.APIView, MyPaginationClass):
    """Отправляет историю запросов."""

    def get(self, request):
        """GET запрос истории."""
        filter_param = request.GET.get('filter')
        queryset = CadastralData.objects.all()
        if filter_param:
            queryset = queryset.filter(cadastral_number=filter_param)
        results = self.paginate_queryset(queryset, request, view=self)
        serializer = HistorySerializer(results, many=True)
        return self.get_paginated_response(serializer.data)
