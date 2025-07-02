from django.core.management import BaseCommand

from diary.models import Tag, Entry
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
        tag5 = Tag.objects.create(name='События', owner=user2)
        tag6 = Tag.objects.create(name='Планы', owner=user2)
        tag7 = Tag.objects.create(name='Тревога', owner=user2)

        # e1 = Entry.objects.create(title=)

        self.stdout.write(self.style.SUCCESS('Данные загружены'))
