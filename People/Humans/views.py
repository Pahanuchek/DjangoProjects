# from django.shortcuts import render, get_object_or_404, redirect
from .models import Humans, Profession
from .forms import HumansForm
from django.views.generic import ListView, DetailView, CreateView


class HumanPage(ListView):
    model = Humans
    context_object_name = 'humans'
    template_name = 'Humans/humans.html'
    extra_context = {'title': 'Главная страница'}

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Сайт о людях'
        return context

    def get_queryset(self):
        return Humans.objects.filter(is_published=True).select_related('profession')


class HumansByProfession(ListView):
    model = Humans
    context_object_name = 'humans'
    template_name = 'Humans/profession.html'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        profession = Profession.objects.get(pk=self.kwargs['profession_id'])
        context['title'] = profession.title
        return context

    def get_queryset(self):
        return Humans.objects.filter(profession_id=self.kwargs['profession_id'], is_published=True).select_related('profession')


class ViewHumans(DetailView):
    model = Humans
    context_object_name = 'human_item'
    template_name = 'Humans/view_humans.html'


class AddHuman(CreateView):
    form_class = HumansForm
    template_name = 'Humans/add_humans.html'


# def view_humans(request, humans_id):
#     # human_item = Humans.objects.get(pk=humans_id)
#     human_item = get_object_or_404(Humans, pk=humans_id)
#     context = {
#         'human_item': human_item
#     }
#     return render(request, 'Humans/view_humans.html', context=context)

# def get_profession(request, profession_id):
#     humans = Humans.objects.filter(profession_id=profession_id)
#     profession_g = Profession.objects.get(pk=profession_id)
#     context = {
#         'humans': humans,
#         'profession_g': profession_g
#     }
#     return render(request, 'Humans/profession.html', context=context)


# def humans(request):
#     humans = Humans.objects.all()
#     context = {
#         'humans' : humans,
#         'title' : 'Сайт о людях',
#     }
#     return render(request, 'Humans/humans.html', context=context)

# def add_humans(request):
#     if request.method == 'POST':
#         form = HumansForm(request.POST)
#         if form.is_valid():
#             # humans = Humans.objects.create(**form.cleaned_data)
#             humans = form.save()
#             return redirect(humans)
#     else:
#         form = HumansForm()
#     return render(request, 'Humans/add_humans.html', {'form': form})

