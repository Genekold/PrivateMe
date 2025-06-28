from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import CreateView, UpdateView, ListView, DetailView

from diary.forms import EntryForm, TagForm
from diary.models import Entry, Tag


class EntryListView(ListView):
    """Класс представления записей."""
    model = Entry
    template_name = "diary/index.html"
    context_object_name = "entrys"

    def get_queryset(self):
        date = timezone.now().date()
        qs = Entry.objects.filter(created_at__date=date)
        return qs


class EntryDetailView(DetailView):
    """Класс детального представления сообщения"""
    model = Entry
    template_name = "diary/entry_detail.html"
    context_object_name = "entry"
    # permission_required = 'diary.view_message'


class EntryCreateView(CreateView):
    """Класс создания записи в дневнике."""
    model = Entry
    form_class = EntryForm
    template_name = "diary/entry_create.html"
    title_page = "Создание записи"
    success_url = reverse_lazy("diary:entry-list")
    # permission_required = 'mailing.add_mailingrecipient'

    def form_valid(self, form):
        entry = form.save(commit=False)
        entry.owner = self.request.user
        return super().form_valid(form)


class EntryUpdateView(UpdateView):
    """Класс изменения записи в дневнике."""
    model = Entry
    form_class = EntryForm
    template_name = "diary/entry_canging.html"
    success_url = reverse_lazy("diary:index")
    # permission_required = 'mailing.change_message'


class TagCreateView(CreateView):
    """Класс для создония тэгов"""
    model = Tag
    form_class = TagForm
    template_name = 'diary/tag_form.html'
    success_url = reverse_lazy('diary:entry-list')

    def form_valid(self, form):
        entry = form.save(commit=False)
        entry.owner = self.request.user
        return super().form_valid(form)


# def index(request):
#     """Функция предтавления главной страницы"""
#
#     return render(request, 'diary/index.html')
