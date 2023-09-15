from rest_framework import serializers

from .models import CadastralData
from .validators import validate_cadastral, validate_coordinates, validate_task


class DataSerializer(serializers.ModelSerializer):
    """Сериализатор кадастровых данных."""

    date = serializers.DateTimeField(format="%d-%m-%Y %H:%M:%S",
                                     read_only=True)

    class Meta:
        fields = ('id', 'cadastral_number', 'longitude', 'latitude', 'date')
        model = CadastralData

    def validate_cadastral_number(self, value):
        """Валидация кадастрового номера."""
        return validate_cadastral(value)

    def validate_longitude(self, value):
        """Валидация долготы."""
        return validate_coordinates(value)

    def validate_latitude(self, value):
        """Валидация широты."""
        return validate_coordinates(value)


class HistorySerializer(DataSerializer):
    """Сериализатор истории кадастровых запросов."""

    class Meta:
        fields = ('id', 'cadastral_number',
                  'longitude', 'latitude', 'result', 'date')
        model = CadastralData


class ResultSerializer(serializers.Serializer):
    """Сериализатор результата."""

    record_id = serializers.IntegerField()
    task_id = serializers.CharField(max_length=36)

    def validate_record_id(self, value):
        """Валидация id объекта."""
        if value < 1:
            raise serializers.ValidationError('Неверный id объекта!')
        return value

    def validate_task_id(self, value):
        """Валидация id задачи."""
        return validate_task(value)
