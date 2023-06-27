from django import forms
import re
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from captcha.fields import CaptchaField

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='Имя пользователя', help_text='Не более 150 символов',
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Адресс электронной почты',
                               widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Введите пароль',
                             widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Подтвердите пароль',
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    captcha = CaptchaField()

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')