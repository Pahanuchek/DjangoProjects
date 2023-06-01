from django.urls import path
from .views import humans


urlpatterns = [
    path('', humans)
]

