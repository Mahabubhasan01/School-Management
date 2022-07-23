from django.contrib import admin
from .models import StudentRegisterForm, StaffRegisterForm, Event, Class_Manager, Subject_Manager
# Register your models here.


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'start_time', 'end_time', ]


@admin.register(Class_Manager)
class ClassAdmin(admin.ModelAdmin):
    list_display = ['id', 'class_name', 'section_name', ]


@admin.register(Subject_Manager)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['id', 'subject_name', 'class_name', 'teacher_name', ]


@admin.register(StudentRegisterForm)
class StudentRegisterFormAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'father_name', 'mother_name', 'father_occupation',
                    'mother_occupation', 'date_of_birth', 'gender', 'blood_group', 'phone_number', 'course', 'section', 'religion']


@admin.register(StaffRegisterForm)
class StaffRegisterFormAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'father_name', 'mother_name', 'subject_choice',
                    'date_of_birth', 'gender', 'blood_group', 'phone_number', 'course', 'section', 'religion']
