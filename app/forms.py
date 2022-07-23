from .models import Class_Manager_Model, Event, Subject_Manager
from django.forms import ModelForm, DateInput
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.contrib.auth.models import User
from django import forms
from .models import StudentRegisterForm


class StudentForm(forms.ModelForm):

    class Meta:
        model = StudentRegisterForm
        fields = ['first_name', 'last_name', 'father_name', 'mother_name', 'father_occupation', 'father_occupation',
                  'date_of_birth', 'gender', 'course', 'section', 'phone_number', 'blood_group', 'religion']

        labels = {'first_name': 'First Name', 'last_name': 'Last Name', 'father_name': 'Father Name', 'mother_name': 'Mother Name', 'father_occupation': 'Father Occupation', 'mother_occupation': 'Mother Occupation',
                  'date_of_birth': 'Date of birth', 'gender': 'Gender', 'course': 'Course', 'section': 'Section', 'phone_number': 'Phone Number', 'blood_group': 'Blood Group', 'religion': 'Religion'}
        widgets = {'first_name': forms.TextInput(
            attrs={'class': 'form-control'}), 'first_name': forms.TextInput(
            attrs={'class': 'form-control'}), 'last_name': forms.TextInput(
            attrs={'class': 'form-control'}), 'father_name': forms.TextInput(
            attrs={'class': 'form-control'}), 'mother_name': forms.TextInput(
            attrs={'class': 'form-control'}), 'first_name': forms.TextInput(
            attrs={'class': 'form-control'}), 'first_name': forms.TextInput(
            attrs={'class': 'form-control'}), }


class user_student(UserCreationForm):
    password1 = forms.CharField(
        label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(
        label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        labels = {'first_name': 'First Name',
                  'last_name': 'Last Name', 'email': 'Email', }
        widgets = {'username': forms.TextInput(attrs={'class': 'form-control'}), 'first_name': forms.TextInput(attrs={'class': 'form-control'}),
                   'last_name': forms.TextInput(attrs={'class': 'form-control'}), 'email': forms.EmailInput(attrs={'class': 'form-control'}), }


class Login_Form(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    password = forms.CharField(label='Password', strip=False, widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'autocomplete': 'current-password'}))


class EventForm(ModelForm):
    class Meta:
        model = Event
        # datetime-local is a HTML5 input type, format to make date time show on fields
        widgets = {
            'start_time': DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
            'end_time': DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
        }
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(EventForm, self).__init__(*args, **kwargs)
        # input_formats parses HTML5 datetime-local input to datetime field
        self.fields['start_time'].input_formats = ('%Y-%m-%dT%H:%M',)
        self.fields['end_time'].input_formats = ('%Y-%m-%dT%H:%M',)


class Subject_Form(ModelForm):
    class Meta:
        model = Subject_Manager
        fields = ['subject_name', 'teacher_name', 'class_name', ]
        labels = {'subject_name': 'Subject Name',
                  'class_name': 'Class Name', 'teacher_name': 'Teacher Name', }
        # widgets = {'username': forms.TextInput(attrs={'class': 'form-control'}), 'first_name': forms.TextInput(attrs={'class': 'form-control'}),
        #            'last_name': forms.TextInput(attrs={'class': 'form-control'}), 'email': forms.EmailInput(attrs={'class': 'form-control'}), }


class Class_Form(ModelForm):
    class Meta:
        model = Class_Manager_Model
        fields = ['class_name', 'section_name', ]
        labels = {
            'class_name': 'Class Name', 'section_name': 'Section Name',
        }
        # widgets = {'username': forms.TextInput(attrs={'class': 'form-control'}), 'first_name': forms.TextInput(attrs={'class': 'form-control'}),
        #            'last_name': forms.TextInput(attrs={'class': 'form-control'}), 'email': forms.EmailInput(attrs={'class': 'form-control'}), }
