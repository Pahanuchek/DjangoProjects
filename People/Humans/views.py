from django.shortcuts import render
from .models import Humans

def humans(request):
    humans = Humans.objects.all()
    context = {
        'humans' : humans,
        'title' : 'Сайт о людях'
    }
    return render(request, 'Humans/humans.html', context=context)
