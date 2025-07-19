from django.contrib.auth import get_user_model
from django.db import models


class Mood(models.TextChoices):
    """Класс настроения записи"""

    MOOD = '👌', 'Норма'
    SMILE = '😊', 'Улыбка'
    LAUGH = '😂', 'Смех'
    SADNESS = '😒', 'Грусть'
    TEARS = '😢', 'Слезы'
    ANGER = '😡', 'Злость'


class Entry(models.Model):
    """Модель записи в дневнике."""

    title = models.CharField(
        max_length=155,
        verbose_name='Заголовок',
    )
    text = models.TextField(verbose_name='Текст записи', help_text='Введите текст записи')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='время создания записи')
    change_time = models.DateTimeField(auto_now=True, verbose_name='время изменения записи')
    tags = models.ManyToManyField('Tag', related_name='entry', blank=True, verbose_name='Теги')
    mood = models.CharField(max_length=5, verbose_name="Настроение", choices=Mood.choices, default=Mood.MOOD)
    owner = models.ForeignKey(
        get_user_model(), verbose_name='Автор записи', related_name='entries', on_delete=models.CASCADE
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'
        ordering = ['-change_time']


class Tag(models.Model):
    """Модель тэга для записи."""

    name = models.CharField(max_length=50, verbose_name='Название тега')
    owner = models.ForeignKey(
        get_user_model(), verbose_name='Автор тэга', related_name='tags', on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'
        ordering = ['name']
