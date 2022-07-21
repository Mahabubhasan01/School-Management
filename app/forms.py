from dataclasses import fields
from django.contrib.auth.forms import UserCreationForm
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
            attrs={'class': 'form-control'}),'first_name': forms.TextInput(
            attrs={'class': 'form-control'}),'last_name': forms.TextInput(
            attrs={'class': 'form-control'}),'father_name': forms.TextInput(
            attrs={'class': 'form-control'}),'mother_name': forms.TextInput(
            attrs={'class': 'form-control'}),'first_name': forms.TextInput(
            attrs={'class': 'form-control'}),'first_name': forms.TextInput(
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
