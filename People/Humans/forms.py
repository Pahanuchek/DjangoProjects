from django import forms
from .models import Profession, Humans
import re
from django.core.exceptions import ValidationError


class HumansForm(forms.ModelForm):

    def clean_name(self):
        name = self.cleaned_data['name']
        if re.match(r'\d', name):
            raise ValueError('Имя не может начинаться с цифры')
        return name

    class Meta:
        model = Humans
        # fields = '__all__'
        fields = ['name', 'biography', 'is_published', 'profession']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'biography': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5
            }),
            'profession': forms.Select(attrs={
                'class': 'form-control',
            })
        }

    # name = forms.CharField(max_length=100, label='Имя', widget=forms.TextInput(attrs={
    #     'class': 'form-control'
    # }))
    # biography = forms.CharField(label='Биография', required=False, widget=forms.Textarea(attrs={
    #     'class': 'form-control',
    #     'rows': 5
    # }))
    # is_published = forms.BooleanField(label='Публикация', initial=True)
    # profession = forms.ModelChoiceField(queryset=Profession.objects.all(), label='Профессия',
    #                                     empty_label='Выберите профессию', widget=forms.Select(attrs={
    #     'class' : 'form-control'
    # }))

