from django.urls import path
from .views import HumanPage, HumansByProfession, ViewHumans, AddHuman
# from .views import humans, get_profession, view_humans, add_humans, register

urlpatterns = [
    path('', HumanPage.as_view(), name='Home'),
    path('profession/<int:profession_id>', HumansByProfession.as_view(), name='Profession'),
    path('humans/<int:pk>', ViewHumans.as_view(), name='View_humans'),
    path('profession/<int:profession_id>/<int:pk>', ViewHumans.as_view(), name='View_humans'),
    path('add_humans', AddHuman.as_view(), name='Add_humans'),
    # path('register', register, name='Register'),
    # path('login', login, name='Login'),


    # path('', humans, name='Home'),
    # path('profession/<int:profession_id>', get_profession, name='Profession'),
    # path('humans/<int:humans_id>', view_humans, name='View_humans'),
    # path('profession/<int:profession_id>/<int:humans_id>', view_humans, name='View_humans'),
    # path('add_humans', add_humans, name='Add_humans')
]

