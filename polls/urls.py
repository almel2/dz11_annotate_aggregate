from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='polls_home'),
    path('book/<int:pk_book>/', views.book_detaile, name='polls_book_detaile'),
    path('book/', views.book_list, name='book_list'),
    path('authors/', views.author_list, name='author_list'),
]
