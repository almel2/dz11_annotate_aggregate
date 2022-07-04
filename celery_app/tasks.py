from celery import shared_task
from django.core.mail import send_mail


@shared_task
def add(x, y):
    return f'result {x} + {y}'


@shared_task
def send_mail_reminder(subject, messages, recipient_list, from_email='exemple@gmail.com'):
    send_mail(subject, messages, from_email=from_email, recipient_list=recipient_list)
