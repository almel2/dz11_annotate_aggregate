from celery import shared_task
from django.core.mail import send_mail
from .parser import parser_qoutes
from dz11_annotate_aggregate.celery import app

from celery.utils.log import get_task_logger  # noqa
logger = get_task_logger(__name__)

@shared_task
def add(x=1, y=1):
    return f'result {x + y}'


@shared_task()
def send_mail_reminder(subject, messages, recipient_list, from_email='exemple@gmail.com'):
    send_mail(subject, messages, from_email=from_email, recipient_list=recipient_list)



@shared_task()
def parser():
    parser_qoutes()

