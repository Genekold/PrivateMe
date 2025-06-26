from django.forms import ModelForm

from diary.models import Entry


class EntryForm(ModelForm):
    """ Форма для добавления записи в дневнике. """
    class Meta:
        model = Entry
        exclude = ['owner', 'created_at', 'change_time']
