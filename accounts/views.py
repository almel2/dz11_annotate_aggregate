from django.shortcuts import render
from django.contrib.auth.views import LogoutView, LoginView, PasswordResetView

def index(request):
    return render(request, 'accounts/base.html', {})


class Logout(LogoutView):
    next_page = 'http://127.0.0.1:8000/'  # редирект на адрес
    # template_name = 'polls/index.html'  # путь на шаблон после выхода


class Login(LoginView):
    next_page = 'http://127.0.0.1:8000/'
    # template_name =  путь на шаблон с формой для входа

class PasswordReset(PasswordResetView):
    pass