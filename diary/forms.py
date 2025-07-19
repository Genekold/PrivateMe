from django import forms

from diary.models import Entry, Tag


class EntryForm(forms.ModelForm):
    """Форма для добавления записи в дневнике."""

    class Meta:
        model = Entry
        fields = [
            'title',
            'text',
            'tags',
            'mood',
        ]
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Введите заголовок записи',
                    'style': 'border-color: indigo; box-shadow: 0 0 0 0.2rem rgba(75, 0, 130, 0.25);',
                }
            ),
            'text': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Введите текст записи',
                    'style': 'border-color: indigo; box-shadow: 0 0 0 0.2rem rgba(75, 0, 130, 0.25);',
                }
            ),
            'tags': forms.SelectMultiple(
                attrs={
                    'class': 'form-control',
                    'style': 'border-color: indigo; box-shadow: 0 0 0 0.2rem rgba(75, 0, 130, 0.25);',
                }
            ),
            'mood': forms.Select(
                attrs={
                    'class': 'form-control',
                    'style': 'border-color: indigo; box-shadow: 0 0 0 0.2rem rgba(75, 0, 130, 0.25);',
                }
            ),
        }
        labels = {
            'title': 'Заголовок',
            'text': 'Текст записи',
            'tags': 'Теги',
            'mood': 'Настроение',
        }

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

        if self.user:
            self.fields['tags'].queryset = Tag.objects.filter(owner=self.user)


class TagForm(forms.ModelForm):
    """Форма для создания тэгов."""

    class Meta:
        model = Tag
        fields = [
            'name',
        ]
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Введите название тега',
                    'style': 'border-color: indigo; box-shadow: 0 0 0 0.2rem rgba(75, 0, 130, 0.25);',
                }
            )
        }
        labels = {'name': 'Название тега'}

    def clean_name(self):
        name = self.cleaned_data['name']
        if Tag.objects.filter(name__iexact=name).exists():
            raise forms.ValidationError("Тег с таким названием уже существует")
        return name
