from django.contrib.auth.forms import UserCreationForm

from users.models import User


class StyleForm:
    """Класс для наследования стилизации форм."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class UserRegisterForm(StyleForm, UserCreationForm):
    class Meta:
        model = User
        fields = ['nickname', 'email', 'password1', 'password2']
