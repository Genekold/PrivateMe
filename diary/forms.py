from django import forms

from diary.models import Entry, Tag


class EntryForm(forms.ModelForm):
    """Форма для добавления записи в дневнике."""

    class Meta:
        model = Entry
        exclude = ['owner', 'created_at', 'change_time']


class TagForm(forms.ModelForm):
    """Форма для создания тэгов."""

    class Meta:
        model = Tag
        fields = [
            'name',
        ]
        widgets = {'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите название тега'})}
        labels = {'name': 'Название тега'}

    def clean_name(self):
        name = self.cleaned_data['name']
        if Tag.objects.filter(name__iexact=name).exists():
            raise forms.ValidationError("Тег с таким названием уже существует")
        return name
