import datetime

from django.core.management import BaseCommand

from diary.models import Entry, Mood, Tag
from users.models import User


class Command(BaseCommand):
    """Класс для пердварительной загрузки данных в базу данных"""

    def handle(self, *args, **options):
        user1 = User.objects.create(nickname='user1', email='user1@mail.ru', is_active=True)
        user1.set_password('Qwe123')
        user1.save()
        user2 = User.objects.create(nickname='user2', email='user2@mail.ru', is_active=True)
        user2.set_password('Qwe123')
        user2.save()

        tag1 = Tag.objects.create(name='Утро', owner=user1)
        tag2 = Tag.objects.create(name='Мои мысли', owner=user1)
        tag3 = Tag.objects.create(name='Идеи', owner=user1)
        tag4 = Tag.objects.create(name='Гнев', owner=user1)
        tag5 = Tag.objects.create(name='Счастье', owner=user1)
        tag6 = Tag.objects.create(name='События', owner=user2)
        tag7 = Tag.objects.create(name='Планы', owner=user2)
        tag8 = Tag.objects.create(name='Тревога', owner=user2)

        e1 = Entry.objects.create(
            title='Приступил делать диплом',
            text="Сегодня приступил к написанию дипломной работы",
            mood=Mood.SMILE,
            owner=user1,
        )
        e1.created_at = datetime.datetime(2025, 7, 1, 6, 00, 00, 358117, tzinfo=datetime.timezone.utc)
        e1.tags.add(tag1)
        e1.save()

        e2 = Entry.objects.create(
            title='Процесс',
            text="Сегодня лучший день для написания кода. Все задуманые идеи воплощаюстя в жизнь с первой попытки",
            mood=Mood.LAUGH,
            owner=user1,
        )
        e2.created_at = datetime.datetime(2025, 7, 1, 12, 12, 10, 358117, tzinfo=datetime.timezone.utc)
        e2.tags.add(tag2)
        e2.save()

        e3 = Entry.objects.create(
            title='Второй день!',
            text="Сегодня второй день пишу диплом. Вчера был продуктивный день. Надеюсь сегодня будет такой же "
            "продуктивный день. За ночь в голове накопилось много идей для реализации в проекте",
            mood=Mood.LAUGH,
            owner=user1,
        )
        e3.created_at = datetime.datetime(2025, 7, 2, 5, 13, 10, 358117, tzinfo=datetime.timezone.utc)
        e3.tags.add(tag2, tag3)
        e3.save()

        e4 = Entry.objects.create(
            title='ААААА', text="Голова кругом! Ничего не выходит! Я устал...", mood=Mood.ANGER, owner=user1
        )
        e4.created_at = datetime.datetime(2025, 7, 2, 15, 00, 10, 358117, tzinfo=datetime.timezone.utc)
        e4.tags.add(tag4)
        e4.save()

        e5 = Entry.objects.create(
            title='Ура!',
            text="К вечеру собрался и все сделал. УРА. Я сдал диплом на проверку!!!",
            mood=Mood.LAUGH,
            owner=user1,
        )
        e5.created_at = datetime.datetime(2025, 7, 2, 20, 00, 10, 358117, tzinfo=datetime.timezone.utc)
        e5.tags.add(tag5)
        e5.save()

        e6 = Entry.objects.create(
            title='Начало',
            text="Ну наконец то я добралась до написания дипломной работы. "
            "Темой моего проекта я выбрала разработку веб приложения  для ведения личного дневника."
            "Сегодня в планах начать проект. Разработать структуру, правильно настроить работу с базой данных",
            owner=user2,
        )
        e6.created_at = datetime.datetime(2025, 7, 1, 6, 00, 10, 358117, tzinfo=datetime.timezone.utc)
        e6.tags.add(tag7)
        e6.save()

        e7 = Entry.objects.create(
            title='Усталый вечер',
            text="Весь день кипела над проектом, устала сильно, медленно, но дело идет. Начала понимать что работы еще"
            "очень много(((",
            mood=Mood.SADNESS,
            owner=user2,
        )
        e7.created_at = datetime.datetime(2025, 7, 1, 20, 00, 10, 358117, tzinfo=datetime.timezone.utc)
        e7.tags.add(tag8)
        e7.save()

        e8 = Entry.objects.create(
            title='Победа',
            text="Я очень хороршо постаралась и наконец то сделала эту дипломную работу. Сдала не проверку."
            " Жду ответа.",
            mood=Mood.SMILE,
            owner=user2,
        )
        e8.created_at = datetime.datetime(2025, 7, 2, 20, 00, 10, 358117, tzinfo=datetime.timezone.utc)
        e8.tags.add(tag6)
        e8.save()

        self.stdout.write(self.style.SUCCESS('Данные загружены'))
