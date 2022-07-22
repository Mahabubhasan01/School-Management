from django.contrib import admin
from .models import StudentRegisterForm, StaffRegisterForm,Event
# Register your models here.

admin.site.register(Event)
@admin.register(StudentRegisterForm)
class StudentRegisterFormAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'father_name', 'mother_name', 'father_occupation',
                    'mother_occupation', 'date_of_birth', 'gender', 'blood_group', 'phone_number', 'course', 'section', 'religion']


@admin.register(StaffRegisterForm)
class StaffRegisterFormAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'father_name', 'mother_name', 'subject_choice',
                    'date_of_birth', 'gender', 'blood_group', 'phone_number', 'course', 'section', 'religion']
