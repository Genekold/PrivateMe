import secrets

from django.contrib.auth.views import PasswordResetView
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from config.settings import EMAIL_HOST_USER
from users.forms import UserRegisterForm, CustomPasswordResetForm
from users.models import User


class UserCreateView(CreateView):
    """Класс для регистрации нового пользователя."""

    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy("users:login")

    def form_valid(self, form):
        user = form.save()
        user.is_active = False
        user.username = user.nickname
        token = secrets.token_hex(16)
        user.token = token
        user.save()
        host = self.request.get_host()
        url = f'http://{host}/users/email-confirm/{token}/'
        send_mail(
            subject='Подтвеждение почты',
            message=f'Перейдите по ссылке для подтверждения почты {url}',
            from_email=EMAIL_HOST_USER,
            recipient_list=[user.email],
        )
        return super().form_valid(form)


def email_verification(request, token):
    """Функция для активации зарегистрированного пользователя при подтверждении почты."""

    user = get_object_or_404(User, token=token)
    user.is_active = True
    user.save()
    return redirect(reverse_lazy('users:login'))


class CustomPasswordResetView(PasswordResetView):
    """Проверка существования пользователя."""

    form_class = CustomPasswordResetForm
    template_name = 'users/password_reset_form.html'
    email_template_name = 'users/password_reset_email.html'
    success_url = reverse_lazy('users:password_reset_done')


def profile(request):
    return render(request, "users/profile.html")
