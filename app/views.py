from .forms import EventForm
import calendar
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from datetime import datetime, timedelta, date
from django.http import HttpResponseRedirect
from .forms import StudentForm, user_student as user
from django.contrib.auth.forms import SetPasswordForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from app.models import StudentRegisterForm, StaffRegisterForm
from .forms import Login_Form
from django.contrib.auth.models import User
# Create your views here.

from .models import *
from datetime import datetime, date
from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.utils.safestring import mark_safe

from .models import *
from .utils import Calendar


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
    return render(request, 'profile.html', {'users': users})


def user_dashboard(request):
    return render(request, 'dashboard.html')


def Navbar_Dashboard(request):
    users = User.objects.all()
    return render(request, 'navbardashboard.html', {'users': users})


def Student_Manager(request):
    student = StudentRegisterForm.objects.all()
    context = {'student': student}
    print(context)
    return render(request, 'studentmanager.html', {'student': student})


def Staff_Manager(request):
    staffs = StaffRegisterForm.objects.all()
    context = {'staffs': staffs}
    print(context)
    return render(request, 'staffmanager.html', {'staffs': staffs})


def Class_Manager(request):
    staffs = StaffRegisterForm.objects.all()
    context = {'staffs': staffs}
    print(context)
    return render(request, 'classmanager.html', {'staffs': staffs})


class CalendarView(generic.ListView):
    model = Event
    template_name = 'calendar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        d = get_date(self.request.GET.get('month', None))
        cal = Calendar(d.year, d.month)
        html_cal = cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)
        context['prev_month'] = prev_month(d)
        context['next_month'] = next_month(d)
        return context


def get_date(req_month):
    if req_month:
        year, month = (int(x) for x in req_month.split('-'))
        return date(year, month, day=1)
    return datetime.today()


def prev_month(d):
    first = d.replace(day=1)
    prev_month = first - timedelta(days=1)
    month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
    return month


def next_month(d):
    days_in_month = calendar.monthrange(d.year, d.month)[1]
    last = d.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
    return month


def event(request, event_id=None):
    instance = Event()
    if event_id:
        instance = get_object_or_404(Event, pk=event_id)
    else:
        instance = Event()

    form = EventForm(request.POST or None, instance=instance)
    if request.POST and form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('calendar'))
    return render(request, 'event.html', {'form': form})


def SubjectManager(request):
    return render(request, 'subjectmanager.html')


def ClassManager(request):
    return render(request, 'classmanager.html')


def ResultManager(request):
    return render(request, 'resultmanager.html')


def FeeManagement(request):
    return render(request, 'feemanagement.html')


def ViewUSers(request):
    users = StaffRegisterForm.objects.all()
    students = StudentRegisterForm.objects.all()
    return render(request, 'viewusers.html', {'users': users, 'students': students})


def StaffPayRoll(request):
    return render(request, 'staffpayroll.html')


def StudentPayment(request):
    return render(request, 'studentpayment.html')


def Class_Six(request):
    return render(request, 'classsix.html')


def Class_Seven(request):
    return render(request, 'classseven.html')


def Class_Eight(request):
    return render(request, 'classeight.html')


def Class_Nine(request):
    return render(request, 'classnine.html')


def Class_Ten(request):
    return render(request, 'classten.html')


def Ssc_Candidate(request):
    return render(request, 'ssccandidate.html')


def Class_Six_Result(request):
    return render(request, 'classsix.html')


def Class_Seven_Result(request):
    return render(request, 'classseven.html')


def Class_Eight_Result(request):
    return render(request, 'classeight.html')


def Class_Nine_Result(request):
    return render(request, 'classnine.html')


def Class_Ten_Result(request):
    return render(request, 'classten.html')


def Ssc_Candidate_Result(request):
    return render(request, 'ssccandidate.html')
