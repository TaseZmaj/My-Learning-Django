from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from decimal import Decimal

# Create your models here.

class Student(models.Model):
    # Replaces the default id created from Django with the index field
    index = models.BigAutoField(primary_key=True, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(null=True, blank=True)
    date_of_birth = models.DateField()

    # RELATIONS =======================================================
        # Many-to-One
        # 1 Student -> 1 Faculty
        # 1 Faculty -> Many Students
    faculty = models.ForeignKey("Faculty", on_delete=models.CASCADE,
                                related_name="students", null=True)
    # ================================================================

    #CHOICES =========================================================
    GENDER_CHOICES = {
        "M": "Male",
        "F": "Female"
    }
    gender = models.CharField(
        max_length=1,
        choices=GENDER_CHOICES
    )
    # ================================================================

    # CHOICES - ENUMERATION ==========================================
    class YearInSchool(models.TextChoices):
        FRESHMAN = "FR", _("Freshman") # "<value>", _("<label>")
        SOPHOMORE = "SO", _("Sophomore")
        JUNIOR = "JR", _("Junior")
        SENIOR = "SR", _("Senior")
        GRADUATE = "GR", _("Graduate")

    year_in_school = models.CharField(
        max_length=2,
        choices=YearInSchool.choices,
        default=YearInSchool.FRESHMAN,
    )

    def about_to_graduate(self):
        return self.year_in_school == self.YearInSchool.GRADUATE
    # ===============================================================

    def get_age(self):
        return timezone.now().date() - self.date_of_birth

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Course(models.Model):
    course_name = models.CharField(max_length=50)
    credits = models.IntegerField(default=6)
    currently_active = models.BooleanField(default=False)

    # RELATIONS =======================================================
        # Many-To-Many
        # 1 Course -> Many Students
        # 1 Student -> Many Courses
    students = models.ManyToManyField(Student, related_name="enrolled_courses")

        # Many-to-One
        # 1 Course -> 1 Faculty
        # 1 Faculty -> Many Courses
    faculty = models.ForeignKey("Faculty", on_delete=models.CASCADE,
                                related_name="courses", null=True)
    # ================================================================

    def __str__(self):
        return f'Course - "{self.course_name}" at Faculty: "{self.faculty.faculty_name}"'


class Faculty(models.Model):
    faculty_name = models.CharField(max_length=50)

    # RANGE on a select field =========================================
    rating = models.DecimalField(
        max_digits=3,
        decimal_places=2,
        default=Decimal('0.00'),
        validators=[
            MinValueValidator(Decimal('0.00')),
            MaxValueValidator(Decimal('10.00'))
        ]
    )
    #==================================================================

    # RELATIONS =======================================================
        # One-to-one
        # 1 faculty may have 1 location
        # that 1 location belongs only to that one faculty
    location = models.OneToOneField("Location",
                                    on_delete=models.CASCADE, null=True)
    # ================================================================

    def __str__(self):
        return f'Faculty - "{self.faculty_name}", Address: {self.location.__str__()}'



class Location(models.Model):
    address = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)


    def __str__(self):
        return f'Location - {self.address}, {self.city}, {self.country}'








