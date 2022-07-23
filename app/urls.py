from . import views
from django.urls import path
urlpatterns = [
    path('base/', views.Base, name='base'),
    path('', views.Home, name='home'),
    path('admin-form/', views.Head_Form, name='Admin_Form'),
    path('staff-form/', views.Staff_Form, name='Staff_Form'),
    path('student-form/', views.Student_Form, name='Student_Form'),
    path('user-student/', views.user_student, name='UserStudent'),
    path('login/', views.user_student_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('change_password/', views.change_password, name='change_password'),
    path('profile/', views.user_profile, name='profile'),
    path('admin_login/', views.user_admin_login, name='admin_login'),
    path('staff_login/', views.user_staff_login, name='staff_login'),
    path('student_manager/', views.Student_Manager, name='student_manager'),
    path('class_manager/', views.Class_Manager, name='class_manager'),
    path('staff_manager/', views.Staff_Manager, name='staff_manager'),
    path('dashboard/', views.user_dashboard, name='dashboard'),
    path('calendar/', views.CalendarView.as_view(), name='calendar'),

    path('event/new/', views.event, name='event_new'),
    path('event/edit/(?P<event_id>\d+)/$', views.event, name='event_edit'),
    path('subject_manager/', views.SubjectManager, name='subject_manager'),
    path('class_manager/', views.ClassManager, name='class_manager'),
    path('result_manager/', views.ResultManager, name='result_manager'),
    path('fee_management/', views.FeeManagement, name='fee_management'),
    path('view_users/', views.ViewUSers, name='view_users'),
    path('staff_pay_roll/', views.StaffPayRoll, name='staff_pay_roll'),
    path('student_payment/', views.StudentPayment, name='student_payment'),

    path('Class_Six/', views.Class_Six, name='class_six'),
    path('Class_Seven/', views.Class_Seven, name='class_seven'),
    path('Class_Eight/', views.Class_Eight, name='class_eight'),
    path('Class_Nine/', views.Class_Nine, name='class_nine'),
    path('Class_Ten/', views.Class_Ten, name='class_ten'),
    path('Ssc_Candidate/', views.Ssc_Candidate, name='ssc_candidate'),


    path('Class_Six_Result/', views.Class_Six_Result, name='class_six_result'),
    path('Class_Seven_Result/', views.Class_Seven_Result, name='class_seven_result'),
    path('Class_Eight_Result/', views.Class_Eight_Result, name='class_eight_result'),
    path('Class_Nine_Result/', views.Class_Nine_Result, name='class_nine_result'),
    path('Class_Ten_Result/', views.Class_Ten_Result, name='class_ten_result'),
    path('Ssc_Candidate_Result/', views.Ssc_Candidate_Result, name='ssc_candidate_result'),


]
