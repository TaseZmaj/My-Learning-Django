from django.urls import path, include

from . import views

app_name = "university"
urlpatterns = [
    path('', views.index, name='index'),
    path('faculty_details/<id>/', views.faculty_details, name='faculty_details'),
    path('add_faculty/', views.add_faculty, name='add_faculty'),
    path('delete_faculty/<id>/', views.delete_faculty, name='delete_faculty'),
    path('add_student/<id>', views.add_student, name='add_student'),
]