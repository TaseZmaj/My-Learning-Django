from django.contrib import admin

from university.models import Faculty, Course, Student, Location

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    #Ovie ke se display-nati vo tabelata
    list_display = ('first_name', 'last_name', 'email', 'get_age', 'get_faculty_name')

    # editable by the admin
    fields = ["first_name", "last_name", "email"]

    #Mesti koi linkovi da pokazuvaat kon add/update page
    list_display_links = ["first_name", "last_name"]

    #Filtrira - prvo po last_name, pa po first_name
    list_filter = ["last_name", "first_name"]

    #Vo samata tabela ovozmozuva editing
    list_editable = ["email"]

    #Generira 1 search input i vo nego shto ke pishesh
    #go matchnuva so values-ot vo nizata
    search_fields = ["first_name", "last_name", "email"]

    #Pravi SQL join na faculty-to
    # nema visible promeni
    list_select_related = ["faculty"]

    #Pagination, Ordering & Performance -------------------------------------------
    list_per_page = 4
    #Ako selektirash "show all", maxsimum br shto moze da pokaze -> 100
    list_max_show_all = 100
    # Sort by last name (ascending)
    #------------------------------------------------------------------------------

    #If you don't do this, Django will automatically use the
    #__str__() method for faculty
    @admin.display(description='Faculty') #column header name
    def get_faculty_name(self, obj):
        return obj.faculty.faculty_name if obj.faculty else 'No faculty'


    def save_model(self, request, obj, form, change):
        # 1. Logic: Force email to lowercase before saving
        if obj.email:
            obj.email = obj.email.lower()

        # 2. Logic: You could check if this is a NEW object or an UPDATE
        if not change:
            # This logic runs only when the object is created
            print(f"User {request.user} is creating a new student: {obj}")

        # IMPORTANT: You must call the parent save_model to actually save!
        super().save_model(request, obj, form, change)

    #ODREDUVA SHTO TOCNO MOZE ADMIN, a sto REGULAR STAFF
    #MEMBER da vidi
    def get_queryset(self, request):
        # 1. Get the base queryset
        qs = super().get_queryset(request)

        # 2. If it's you (the superuser), show all students
        if request.user.is_superuser:
            return qs

        # 3. If it's a regular staff member, only show students
        # from the "Engineering" faculty (as an example)
        return qs.filter(faculty__faculty_name="FINKI")



@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    #customizes the admin add/update page
    fieldsets = [
        (None, {"fields": ["course_name","currently_active" ]}),
        ("Advanced Options",
            {
                "classes": ["collapse"],
                "fields": ["students", "credits"]
            }
        )
    ]

    def delete_model(self, request, obj):
        # Logic: Log the course being deleted
        print(f"WARNING: Course {obj.course_name} is being deleted by {request.user}")

        # Optional: You could perform extra cleanup here
        # (e.g., deleting related files on the server)

        super().delete_model(request, obj)

# TabularInline shows them in a compact table-like row
class StudentInline(admin.TabularInline):
    model = Student
    extra = 1  # This shows 1 empty row by default for
               # adding a new student quickly

class LocationInline(admin.StackedInline):
    model = Location
    extra = 1


@admin.register(Faculty)
class FacultyAdmin(admin.ModelAdmin):
    inlines = [StudentInline, LocationInline]

    list_display = ("faculty_name", "rating", "location")

    # don't show "rating" in the add/update page
    exclude = ["rating"]


    #ILI exclude koristis ILI OVA:
    readonly_fields = ["rating"]

    ordering = ("rating", "-faculty_name")
    # To sort descending, add a minus sign:
    # ordering = ("-rating",)
    # You can also use multiple fields:
    # Sort by last name, then by first name for people with the same last name
    # ordering = ("last_name", "first_name")

    list_select_related = ["location"]



@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):

    list_display=('__str__','address', 'city', 'country', 'image')

    #koga ima nekoj empty value - pokazuva "-empty"
    empty_value_display = "-empty-"





# Register your models here.
# admin.site.register(Student)
# admin.site.register(Course)
# admin.site.register(Faculty)
# admin.site.register(Location)