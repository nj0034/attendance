from django.urls import path
from django.contrib.auth import views as auth_views
from accounts import views as accounts_views
from subjects import views as subjects_views
from state import views as state_views

app_name = 'api'

urlpatterns = [
    # accounts
    path('signup', accounts_views.SignUp.as_view()),
    # path('signin', auth_views.LoginView.as_view(template_name='login.html')),
    path('signin', accounts_views.SignIn.as_view()),
    path('signout', auth_views.LogoutView.as_view(template_name='registration/logged_out.html')),

    # attendance
    path('number', state_views.RandomNumber.as_view()),
    path('check_attendance', state_views.CheckAttendance.as_view()),
    path('manage_attendance', state_views.ManageAttendance.as_view()),

    # subjects
    path('subjects/professor', subjects_views.ProfessorSubjectList.as_view()),
    path('subjects/student', subjects_views.StudentSubjectList.as_view()),
    path('subject', subjects_views.SubjectManagement.as_view()),

    # week
    path('week', subjects_views.WeekInfo.as_view()),
]