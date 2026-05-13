from django.urls import path, include

from . import views

app_name = "university"
urlpatterns = [
    path('', views.index, name='index')
]