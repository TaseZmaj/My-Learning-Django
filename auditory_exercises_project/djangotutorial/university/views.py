from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404

from university.models import Faculty, Student
from university.forms import FacultyForm, StudentForm

# Create your views here.

def index(request):
    faculties = Faculty.objects.all()
    students = Student.objects.all()

    context = {
        "faculties": faculties,
        "students": students,
        "pageTitle": "University Home Page"
    }
    return render(request, 'index.html',context)

# @login_required
def faculty_details(request, id):
    try:
        faculty = Faculty.objects.get(id=id)
        students = Student.objects.filter(faculty=faculty)
        context = {
            "faculty": faculty,
            "students": students
        }
    except Faculty.DoesNotExist:
        raise Http404("Faculty does not exist")

    return render(request, "details.html", context)

@login_required
def add_faculty(request):
    if request.method == "POST":
        form = FacultyForm(request.POST, request.FILES)
        if form.is_valid():
            faculty = form.save(commit=False)
            faculty.save()
            return redirect("university:index")
    form = FacultyForm()
    context = {
        "form": form
    }
    return render(request, "add_faculty.html", context)

@login_required
def delete_faculty(request, id):
    if request.method == "POST":
        faculty = Faculty.objects.get(id=id)
        faculty.delete()
    return redirect("university:index")

@login_required
def add_student(request, id):
    faculty = Faculty.objects.get(id=id)
    if request.method == "POST":
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            # first_name = form.cleaned_data['first_name']
            # last_name = form.cleaned_data['last_name']
            # email = form.cleaned_data['email']
            # date_of_birth = form.cleaned_data['date_of_birth']
            student = form.save(commit=False)
            student.save()
            faculty.students.add(student)
            faculty.save()
            return redirect("university:faculty_details", id=id)
    else:
        form = StudentForm()

    context = {
        "form": form,
        "faculty": faculty
    }
    return render(request, "add_student.html", context)