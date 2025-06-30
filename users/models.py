from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Класс пользователя."""

    username = None
    nickname = models.CharField(max_length=155, unique=True, verbose_name="Ник")
    email = models.EmailField(unique=True, verbose_name='Email')
    phone = models.CharField(max_length=20, verbose_name='Телефон', blank=True, null=True)
    avatar = models.ImageField(
        upload_to='users/avatars//%Y/%m/%d/',
        verbose_name='Аватвр',
        blank=True,
        null=True,
        default='/media/users/avatars/default.jpg',
    )
    tg_chat_id = models.CharField(
        max_length=50,
        verbose_name="chat-id в телеграмм",
        help_text="Укажите chat-id в телеграмм",
    )
    created_at = models.DateField(auto_now_add=True, verbose_name='Дата регистрации')

    token = models.CharField(max_length=100, verbose_name='Token', blank=True, null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользоатель'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.nickname
