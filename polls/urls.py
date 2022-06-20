from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='polls_home'),
    path('book/', views.book_list, name='book_list'),
]
