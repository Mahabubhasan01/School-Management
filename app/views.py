from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import StudentForm, user_student as user
from django.contrib.auth.forms import SetPasswordForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from app.models import StudentRegisterForm
from .forms import Login_Form
from django.contrib.auth.models import User
# Create your views here.


def Base(request):
    return render(request, 'base.html', {'home': 'home'})


def Home(request):
    return render(request, 'home.html', {'home': 'home'})


def Head_Form(request):
    return render(request, 'adminform.html', {'admin-form': 'admin-form'})


def Staff_Form(request):
    return render(request, 'staffform.html', {'Staff-form': 'Staff-form'})


def Student_Form(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/user-student/')
    else:
        form = StudentForm()

    return render(request, 'studentform.html', {'form': form})


def Dashboard(request):
    return render(request, 'dashboard.html')


def user_student_login(request):
    fm = Login_Form(request=request, data=request.POST)
    if fm.is_valid():
        username = fm.cleaned_data['username']
        userpassword = fm.cleaned_data['password']
        usr = authenticate(username=username, password=userpassword)
        if usr is not None:
            login(request, usr)
            return HttpResponseRedirect('/dashboard/')
    else:
        fm = Login_Form()
    return render(request, 'login.html', {'form': fm})


def user_admin_login(request):
    fm = Login_Form(request=request, data=request.POST)
    if fm.is_valid():
        username = fm.cleaned_data['username']
        userpassword = fm.cleaned_data['password']
        usr = authenticate(username=username, password=userpassword)
        if usr is not None:
            login(request, usr)
            return HttpResponseRedirect('/dashboard/')
    else:
        fm = Login_Form()
    return render(request, 'adminlogin.html', {'form': fm})


def user_staff_login(request):
    fm = Login_Form(request=request, data=request.POST)
    if fm.is_valid():
        username = fm.cleaned_data['username']
        userpassword = fm.cleaned_data['password']
        usr = authenticate(username=username, password=userpassword)
        if usr is not None:
            login(request, usr)
            return HttpResponseRedirect('/dashboard/')
    else:
        fm = Login_Form()
    return render(request, 'stafflogin.html', {'form': fm})


def change_password(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            fm = SetPasswordForm(user=request.user, data=request.POST)
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(request, fm.user)
                return HttpResponseRedirect('/profile/')
        else:
            fm = SetPasswordForm(user=request.user)
            return render(request, 'changepassword.html', {'form': fm})
    else:
        HttpResponseRedirect('/login/')


def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')


def user_student(request):
    if request.method == 'POST':
        form = user(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/dashboard/')
    else:
        form = user()
    return render(request, 'userStudent.html', {'form': form})


def user_profile(request):
    users = User.objects.all()
    return render(request, 'profile.html',{'users': users})


def user_dashboard(request):
    return render(request, 'dashboard.html')


def Student_Manager(request):
    student = StudentRegisterForm.objects.all()
    context = {'student': student}
    print(context)
    return render(request, 'studentmanager.html', {'student': student})
