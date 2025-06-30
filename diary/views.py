from datetime import datetime

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import CreateView, UpdateView, ListView, DetailView, DeleteView

from diary.forms import EntryForm, TagForm
from diary.models import Entry, Tag


class EntryListView(LoginRequiredMixin, ListView):
    """Класс представления записей."""
    model = Entry
    template_name = "diary/index.html"
    context_object_name = "entrys"

    def get_queryset(self):

        qs = super().get_queryset()

        if filter_date := self.request.GET.get('date'):
            date = datetime.strptime(filter_date, '%d.%m.%Y').date()
            qs = qs.filter(created_at__date=date)
        return qs


class EntryDetailView(LoginRequiredMixin, DetailView):
    """Класс детального представления сообщения"""
    model = Entry
    template_name = "diary/entry_detail.html"
    context_object_name = "entry"
    # permission_required = 'diary.view_message'


class EntryCreateView(LoginRequiredMixin, CreateView):
    """Класс создания записи в дневнике."""
    model = Entry
    form_class = EntryForm
    template_name = "diary/entry_form.html"
    title_page = "Создание записи"
    context_object_name = "entry"
    success_url = reverse_lazy("diary:entry-list")
    # permission_required = 'diary.add_mailingrecipient'

    def form_valid(self, form):
        entry = form.save(commit=False)
        entry.owner = self.request.user
        return super().form_valid(form)


class EntryUpdateView(LoginRequiredMixin, UpdateView):
    """Класс изменения записи в дневнике."""
    model = Entry
    form_class = EntryForm
    template_name = "diary/entry_canging.html"
    success_url = reverse_lazy("diary:entry-list")
    # permission_required = 'diary.change_message'


class EntryDeleteView(LoginRequiredMixin, DeleteView):
    """Класс удаления записи."""
    model = Entry
    success_url = reverse_lazy("diary:entry-list")


class TagCreateView(LoginRequiredMixin, CreateView):
    """Класс для создония тэгов."""
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
