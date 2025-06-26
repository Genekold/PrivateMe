from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from diary.forms import EntryForm
from diary.models import Entry
from users.models import User


class EntryCreateView(CreateView):
    """Класс создания получателя"""
    model = Entry
    form_class = EntryForm
    template_name = "diary/entry_create.html"
    title_page = "Создание записи"
    # success_url = reverse_lazy("dairy:entry_create")  # перенапрвление после создания
    # permission_required = 'mailing.add_mailingrecipient'

    def form_valid(self, form):
        recipient = form.save(commit=False)
        recipient.author = self.request.user
        return super().form_valid(form)


def index(request):
    """Функция предтавления главной страницы"""

    users = User.objects.all()

    context = {
        'users': users,
        'count': users.count()
    }
    return render(request, 'diary/index.html', context=context)
