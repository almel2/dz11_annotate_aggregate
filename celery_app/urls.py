from django.urls import path
from celery_app import views

urlpatterns = [
    path('', views.reminder, name='celery_reminder'),
]