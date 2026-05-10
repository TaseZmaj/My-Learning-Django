from django.contrib import admin

from university.models import Faculty, Course, Student, Location

# Register your models here.
admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Faculty)
admin.site.register(Location)