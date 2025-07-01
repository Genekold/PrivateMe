from datetime import datetime

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.db.models import Q
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from diary.forms import EntryForm, TagForm
from diary.models import Entry, Tag


class EntryListView(ListView):
    """Класс представления записей."""

    model = Entry
    template_name = "diary/index.html"
    context_object_name = "entrys"

    def get_queryset(self):
        qs = super().get_queryset()

        if self.request.user.is_authenticated:
            qs = qs.filter(owner=self.request.user)
        else:
            return qs.none()

        if filter_date := self.request.GET.get('date'):
            date = datetime.strptime(filter_date, '%d.%m.%Y').date()
            qs = qs.filter(created_at__date=date)
        else:
            today = timezone.now().date()
            qs = qs.filter(created_at__date=today)
        return qs


class EntryDetailView(LoginRequiredMixin, DetailView):
    """Класс детального представления сообщения"""

    model = Entry
    template_name = "diary/entry_detail.html"
    context_object_name = "entry"

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.owner != self.request.user:
            raise PermissionDenied("У вас нет прав для просмотра этой записи")

        return super().dispatch(request, *args, **kwargs)


class EntryCreateView(LoginRequiredMixin, CreateView):
    """Класс создания записи в дневнике."""

    model = Entry
    form_class = EntryForm
    template_name = "diary/entry_form.html"
    title_page = "Создание записи"
    context_object_name = "entry"
    success_url = reverse_lazy("diary:entry-list")

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

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

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.owner != self.request.user:
            raise PermissionDenied("У вас нет прав для просмотра этой записи")
        return super().dispatch(request, *args, **kwargs)


class EntryDeleteView(LoginRequiredMixin, DeleteView):
    """Класс удаления записи."""

    model = Entry
    success_url = reverse_lazy("diary:entry-list")

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.owner != self.request.user:
            raise PermissionDenied("У вас нет прав для просмотра этой записи")
        return super().dispatch(request, *args, **kwargs)


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


def search_view(request):
    query = request.GET.get('result', '')
    results = []

    if query:
        results = Entry.objects.filter(Q(title__icontains=query) | Q(text__icontains=query), owner=request.user)

    context = {
        'results': results,
        'query': query
    }
    return render(request, 'diary/search.html', context)
