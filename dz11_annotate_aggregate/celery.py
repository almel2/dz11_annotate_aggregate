import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dz11_annotate_aggregate.settings')

app = Celery('dz11_annotate_aggregate')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.beat_shedule = {}
