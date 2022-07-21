from . import views
from django.urls import path
urlpatterns = [
    path('base/', views.Base, name='base'),
    path('', views.Home, name='home'),
    path('admin-form/', views.Head_Form, name='Admin_Form'),
    path('staff-form/', views.Staff_Form, name='Staff_Form'),
    path('student-form/', views.Student_Form, name='Student_Form'),
    path('user-student/', views.user_student, name='UserStudent'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('change_password/', views.change_password, name='change_password'),
    path('profile/', views.user_profile, name='profile'),
    path('admin_login/', views.user_admin_login, name='admin_login'),
    path('staff_login/', views.user_staff_login, name='staff_login'),
    path('dashboard/', views.user_dashboard, name='dashboard'),

]
