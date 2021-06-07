from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from django.contrib.auth.models import User


class CustomUserCreationForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        self.fields['username'].help_text = ''
        self.fields['username'].label = ''
        self.fields['password1'].help_text = ''
        self.fields['password1'].label = ''
        self.fields['password2'].help_text = ''
        self.fields['password2'].label = ''

        self.fields['password1'].widget.attrs.update(
            {'name': 'password', 'type': 'password', 'placeholder': 'Пароль', 'class': 'password',
             'id': 'userPassword'})
        self.fields['password2'].widget.attrs.update(
            {'name': 'password', 'type': 'password', 'placeholder': 'Повтор пароля', 'class': 'password',
             'id': 'userPassword'})

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(
                attrs={'name': 'username', 'id': 'userLogin', 'placeholder': 'Введите логин', 'class': 'input'})
        }


class LoginUserForm(AuthenticationForm):
    def __init__(self, request=None, *args, **kwargs):
        self.request = request
        self.user_cache = None
        super(AuthenticationForm, self).__init__(*args, **kwargs)
        self.username_field = User._meta.get_field(User.USERNAME_FIELD)
        self.fields['username'].widget.attrs.update(
            {'name': 'username', 'placeholder': 'Логин', 'class': 'input', 'id': 'userLogin'})
        self.fields['password'].widget.attrs.update(
            {'name': 'password', 'placeholder': 'Пароль', 'class': 'input', 'type': 'password', 'id': 'userPassword'})
        self.fields['password'].label = ''
        self.fields['username'].label = ''
        self.error_messages['invalid_login'] = 'Please enter correct values'
