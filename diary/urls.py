from django.urls import path

from diary.apps import DiaryConfig
from diary.views import EntryCreateView, index

app_name = DiaryConfig.name

urlpatterns = [
    path("", index, name='index'),
    path("diary/create/", EntryCreateView.as_view(), name='diary-create'),

]