from django.urls import path
from accounts import views

urlpatterns = [
    path('', views.index, name='accounts_home'),
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', views.Logout.as_view(), name='logout'),
    path('password_reset/', views.PasswordReset.as_view(), name='password_reset'),
]