from django.urls import path
from django.urls import include, path

from . import views


urlpatterns = [
    #Mapiranje na urlto "" (prazen string) na funkcijata index vo views.py
    path("", views.index, name="index"), 
]