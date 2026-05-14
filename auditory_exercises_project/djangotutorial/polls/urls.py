from django.urls import path
from django.urls import include, path

from . import views


app_name = 'polls' #<- BITNO!!
urlpatterns = [
    #Mapiranje na url "/polls" so function index() vo views.py
    path("", views.index, name="index"),

    #Mapiranje na url "/polls/details" so function polls_details() vo views.py
    path("details", views.polls_details, name="details")
]