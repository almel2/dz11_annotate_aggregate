import os
from datetime import timedelta

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dz11_annotate_aggregate.settings')

app = Celery('dz11_annotate_aggregate')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'test_beat': {
        'task': 'celery_app.tasks.parser',
        'schedule': crontab(minute='*/1'),
    },
     #  'test_beat': {
     #          'task': 'celery_app.tasks.send_mail_reminder',
     #          'schedule': crontab(minute='*/1'),
     #      }
}

