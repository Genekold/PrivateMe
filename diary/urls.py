from django.urls import path

from diary.apps import DiaryConfig
from diary.views import EntryCreateView, EntryUpdateView, EntryListView, TagCreateView, EntryDetailView, EntryDeleteView

app_name = DiaryConfig.name

urlpatterns = [
    path("", EntryListView.as_view(), name="entry-list"),
    path("diary/entry/create/", EntryCreateView.as_view(), name='entry-create'),
    path("diary/entry/<int:pk>/", EntryDetailView.as_view(), name="entry-detail"),
    path("diary/entry/<int:pk>/update/", EntryUpdateView.as_view(), name='entry-update'),
    path("message/entry/<int:pk>pk/delete/", EntryDeleteView.as_view(), name="entry-delete"),

    path('diary/tag/create/', TagCreateView.as_view(), name='tag-create'),
]
