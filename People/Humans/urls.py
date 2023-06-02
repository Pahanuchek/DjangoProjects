from django.urls import path
from .views import humans, get_profession, view_humans, add_humans


urlpatterns = [
    path('', humans, name='Home'),
    path('profession/<int:profession_id>', get_profession, name='Profession'),
    path('humans/<int:humans_id>', view_humans, name='View_humans'),
    path('profession/<int:profession_id>/<int:humans_id>', view_humans, name='View_humans'),
    path('add_humans', add_humans, name='Add_humans')
]

