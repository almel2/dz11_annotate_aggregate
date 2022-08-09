from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.Index.as_view(), name='polls_home'),
    # path('', views.index, name='polls_home'),

    path('book/<int:pk_book>/', views.BookDetaile.as_view(), name='polls_book_detaile'),
    # path('book/<int:pk_book>/', views.book_detaile, name='polls_book_detaile'),
    path('book/', views.BookList.as_view(), name='book_list'),
    # path('book/', views.book_list, name='book_list'),

    path('author/<int:pk_author>/', views.AuthorDetaile.as_view(), name='author_detaile'),
    # path('author/<int:pk_author>/', views.authors_detaile, name='author_detaile'),
    path('author/', views.AuthorsList.as_view(), name='author_list'),
    # path('author/', views.author_list, name='author_list'),

    path('store/<int:pk_store>/', views.StoreDetaile.as_view(), name='store_detaile'),
    # path('store/<int:pk_store>/', views.store_detaile, name='store_detaile'),
    path('store/', views.StoreList.as_view(), name='store_list'),
    # path('store/', views.store_list, name='store_list'),

    path('publisher/<int:pk_publisher>/', views.PublisherDetaile.as_view(), name='publisher_detaile'),
    # path('publisher/<int:pk_publisher>/', views.publisher_detaile, name='publisher_detaile'),
    path('publisher/', views.PublisherList.as_view(), name='publisher_list'),
    # path('publisher/', views.publisher_list, name='publisher_list'),
    path('store-add/', views.store_add, name='store_add_form'),

    path('success/', views.success, name='success'),

    path('accounts/login/', auth_views.LoginView.as_view()),
]
