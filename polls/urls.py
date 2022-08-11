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
    #path('store-add/', views.store_add, name='store_add_form'),
    path('store-add/', views.StoreAdd.as_view(), name='store_add_form'),
    path('store-update/<int:pk_store>/', views.StoreUpdate.as_view(), name='store_update'),
    path('store-delete/<int:pk_store>/', views.StoreDelete.as_view(), name='store_delete'),

    path('publisher/<int:pk_publisher>/', views.PublisherDetaile.as_view(), name='publisher_detaile'),
    # path('publisher/<int:pk_publisher>/', views.publisher_detaile, name='publisher_detaile'),
    path('publisher/', views.PublisherList.as_view(), name='publisher_list'),
    # path('publisher/', views.publisher_list, name='publisher_list'),
    path('publisher-add/', views.PublisherAdd.as_view(), name='publisher_add_form'),
    path('publisher-update/<int:pk_publisher>/', views.PublisherUpdate.as_view(), name='publisher_update'),
    path('publisher-delete/<int:pk_publisher>/', views.PublisherDelete.as_view(), name='publisher_delete'),

    path('success/', views.success, name='success'),
]
