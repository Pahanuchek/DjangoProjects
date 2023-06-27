from django import forms
from django.contrib.auth.forms import AuthenticationForm


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Имя пользователя', help_text='Не более 150 символов',
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Введите пароль',
                             widget=forms.PasswordInput(attrs={'class': 'form-control'}))
