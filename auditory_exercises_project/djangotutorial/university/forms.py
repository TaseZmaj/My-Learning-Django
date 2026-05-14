from django.forms import ModelForm
from university.models import Faculty, Student
from django import forms

class FacultyForm(ModelForm):
    class Meta:
        model = Faculty
        exclude = ('id',)

    def __init__(self, *args, **kwargs):
        super(FacultyForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

# class StudentForm(ModelForm):
#     first_name = forms.CharField(
#         widget = forms.TextInput(),
#         max_length=100,
#         label='First Name',)
#
#     last_name = forms.CharField(
#         widget = forms.Textarea(),
#         help_text = 'The last name goes here'
#     )
#
#     nickname = forms.CharField(
#         widget = forms.TextInput(),
#     )
#
#     email = forms.EmailField()
#
#     date_of_birth = forms.DateField()
#
#     # gender = forms.ChoiceField(choices = GENDER_CHOICES,)
#     #
#     # year_in_school = forms.ChoiceField(choices = YearInSchool.choices)
#
#     # faculty = forms.ChoiceField(
#     #     queryset = Faculty.objects.all()
#     # )
#
#     class Meta:
#         model = Student
#         exclude = ('index',)
#
#     def __init__(self, *args, **kwargs):
#         super(StudentForm, self).__init__(*args, **kwargs)
#         for field_name, field in self.fields.items():
#             field.widget.attrs['class'] = 'form-control'
#
class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'email', 'gender', 'date_of_birth', 'year_in_school']
        # exclude = ('index',)

    def __init__(self, *args, **kwargs):
        super(StudentForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'