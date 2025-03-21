from django.urls import path, include

from . import views
from aiutorapp.views import view_enrolled_students  # Import the view_enrolled_students function


urlpatterns = [
    path('view_enrolled_students/<int:course_id>/', views.view_enrolled_students, name='view_enrolled_students'),  # Add URL for viewing enrolled students


    path('dashboard/', views.student_dashboard, name='student_dashboard'),
    path('privacy-policy/', views.privacy_policy, name='privacy_policy'),
    path('terms-of-service/', views.terms_of_service, name='terms_of_service'),

    path('logout/', views.logout_view, name='logout'),  # Added logout URL

    path('teacher_dashboard/', views.teacher_dashboard, name='teacher_dashboard'),
    path('', views.index, name='indexpage'),
    path('Courses/', views.courses, name='courses'),
    path('About/', views.about, name='about'),
    path('Contact/', views.contact, name='contact'),
    path('signin/', views.signin, name='signin'),
    path('signup/', views.signup, name='signup'),
    path('create_course/', views.create_course, name='create_course'),  # New URL pattern for creating a course
    path('enroll_course/<int:course_id>/', views.enroll_course, name='enroll_course'),  # New URL pattern for enrolling in a course
]
