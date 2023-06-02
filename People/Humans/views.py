from django.shortcuts import render
from .models import Humans, Profession

def humans(request):
    humans = Humans.objects.all()
    context = {
        'humans' : humans,
        'title' : 'Сайт о людях',
    }
    return render(request, 'Humans/humans.html', context=context)

def get_profession(request, profession_id):
    humans = Humans.objects.filter(profession_id=profession_id)
    profession_g = Profession.objects.get(pk=profession_id)
    context ={
        'humans' : humans,
        'profession_g' : profession_g
    }
    return render(request, 'Humans/profession.html', context=context)
