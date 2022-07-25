from django.contrib import admin
from .models import Class_Manager_Model, StudentRegisterForm, StaffRegisterForm, Event, Subject_Manager
# Register your models here.


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'start_time', 'end_time', ]


@admin.register(Class_Manager_Model)
class ClassAdmin(admin.ModelAdmin):
    list_display = ['id', 'class_name', 'section_name', ]


@admin.register(Subject_Manager)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['id', 'subject_name', 'class_name', 'teacher_name', ]


@admin.register(StudentRegisterForm)
class StudentRegisterFormAdmin(admin.ModelAdmin):
    list_display = ['id', 'student_name', 'admission_roll',  'email_address', 'student_class',  'father_name', 'mother_name', 'father_occupation',
                    'mother_occupation', 'date_of_birth', 'gender', 'blood_group', 'phone_number', 'course', 'section', 'religion', 'address',  'profile_img', ]


@admin.register(StaffRegisterForm)
class StaffRegisterFormAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'father_name', 'mother_name', 'subject_choice',
                    'date_of_birth', 'gender', 'blood_group', 'phone_number', 'course', 'section', 'religion']
