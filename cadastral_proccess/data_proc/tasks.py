import requests

from django.shortcuts import get_object_or_404
from cadastral_proccess.celery import app
from .models import CadastralData


@app.task(bind=True, max_retries=2, task_track_started=True)
def send_request(self, data, id):
    """Отправка запроса на внешний сервер."""
    try:
        response = requests.get('http://remote_server:8001/data', params=data)
        obj = get_object_or_404(CadastralData, id=id)
        obj.result = response.json()['result']
    except Exception as e:
        print('Ошибка:', e)
        raise
    else:
        obj.save()
        return 'done'
