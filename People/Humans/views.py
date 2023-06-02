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
