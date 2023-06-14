from django import template
from Humans.models import Profession
from django.db.models import Count, F

register = template.Library()

@register.simple_tag(name='get_list_profession')
def get_profession():
    return Profession.objects.all()

@register.inclusion_tag('Humans/list_profession.html')
def show_profession(arg_1='Profession', arg_2 = 'list'):
    #profession = Profession.objects.all()
    profession = Profession.objects.annotate(cnt=Count('humans', filter=F('humans__is_published'))).filter(cnt__gt=0)
    return {'profession': profession, 'arg_1': arg_1, 'arg_2': arg_2}