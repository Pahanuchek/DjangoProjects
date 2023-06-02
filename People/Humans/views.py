from django.shortcuts import render
from .models import Humans, Profession

def humans(request):
    humans = Humans.objects.all()
    profession = Profession.objects.all()
    context = {
        'humans' : humans,
        'title' : 'Сайт о людях',
        'profession': profession
    }
    return render(request, 'Humans/humans.html', context=context)

def get_profession(request, profession_id):
    humans = Humans.objects.filter(profession_id=profession_id)
    professions = Profession.objects.all()
    profession_g = Profession.objects.get(pk=profession_id)
    context ={
        'humans' : humans,
        'professions' : professions,
        'profession_g' : profession_g
    }
    return render(request, 'Humans/profession.html', context=context)
