from django.urls import path

from diary.apps import DiaryConfig
from diary.views import (
    EntryCreateView,
    EntryDeleteView,
    EntryDetailView,
    EntryListView,
    EntryUpdateView,
    TagCreateView,
    search_view,
)

app_name = DiaryConfig.name

urlpatterns = [
    path("", EntryListView.as_view(), name="entry-list"),
    path("diary/entry/create/", EntryCreateView.as_view(), name='entry-create'),
    path("diary/entry/<int:pk>/", EntryDetailView.as_view(), name="entry-detail"),
    path("diary/entry/<int:pk>/update/", EntryUpdateView.as_view(), name='entry-update'),
    path("message/entry/<int:pk>/delete/", EntryDeleteView.as_view(), name="entry-delete"),
    path('diary/tag/create/', TagCreateView.as_view(), name='tag-create'),
    path('search/', search_view, name='search'),
]
