from django.urls import include, path

from classroom.views import classroom, students, teachers

urlpatterns = [
    path('', include('classroom.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', classroom.SignUpView.as_view(), name='signup'),
    #refer classroom/views/classroom.py > class SignUpView
    path('accounts/signup/student/', students.StudentSignUpView.as_view(), name='student_signup'),
    #refer classroom/views/students.py > class StudentSignUpView
    path('accounts/signup/teacher/', teachers.TeacherSignUpView.as_view(), name='teacher_signup'),
    #refer classroom/views/teachers.py > class TeacherSignUpView
]
