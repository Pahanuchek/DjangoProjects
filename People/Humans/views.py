from django.shortcuts import render, get_object_or_404
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

def view_humans(request, humans_id):
    # human_item = Humans.objects.get(pk=humans_id)
    human_item = get_object_or_404(Humans, pk=humans_id)
    context = {
        'human_item': human_item
    }
    return render(request, 'Humans/view_humans.html', context=context)

