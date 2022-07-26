from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'start_time', 'end_time', ]


@admin.register(Class_Manager_Model)
class ClassAdmin(admin.ModelAdmin):
    list_display = ['id', 'teacher_name', 'subject_name',
                    'class_serial', 'class_name', 'section_name', ]


@admin.register(Subject_Manager)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['id', 'subject_name', 'class_name', 'teacher_name', ]


@admin.register(StudentRegisterForm)
class StudentRegisterFormAdmin(admin.ModelAdmin):
    list_display = ['id', 'student_name', 'admission_roll',  'email_address', 'student_class',  'father_name', 'mother_name', 'father_occupation',
                    'mother_occupation', 'date_of_birth', 'gender', 'blood_group', 'phone_number', 'course', 'section', 'religion', 'address',  'profile_image', ]


@admin.register(StaffRegisterForm)
class StaffRegisterFormAdmin(admin.ModelAdmin):
    list_display = ['id', 'student_name', 'admission_roll',  'email_address', 'student_class',  'father_name', 'mother_name', 'father_occupation',
                    'mother_occupation', 'date_of_birth', 'gender', 'blood_group', 'phone_number', 'course', 'section', 'religion', 'address',  'profile_image', ]


@admin.register(Student_Exam)
class StudentExamAdmin(admin.ModelAdmin):
    list_display = ['id', 'terms_name', 'class_name',
                    'section_name', 'start_date', 'end_date', ]


@admin.register(Student_Result)
class StudentResultAdmin(admin.ModelAdmin):
    list_display = ['id', 'terms_name', 'class_name',
                    'section_name', 'published_date', 'attached_file']
