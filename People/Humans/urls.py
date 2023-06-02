from django.urls import path
from .views import humans, get_profession


urlpatterns = [
    path('', humans, name='Home'),
    path('profession/<int:profession_id>', get_profession, name='Profession')
]

