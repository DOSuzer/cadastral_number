import os

from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cadastral_proccess.settings')

app = Celery('cadastral_proccess', broker='redis://redis:6379/0')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()
