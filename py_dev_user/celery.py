import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'py_dev_user.settings')

app = Celery('py_dev_user')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()
