from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.student_dashboard, name='student_dashboard'),
    path('logout/', views.logout_view, name='logout'),  # Added logout URL

    path('teacher_dashboard/', views.teacher_dashboard, name='teacher_dashboard'),
    path('', views.index, name='indexpage'),
    path('Courses/', views.courses, name='courses'),
    path('About/', views.about, name='about'),
    path('Contact/', views.contact, name='contact'),
    path('signin/', views.signin, name='signin'),
    path('signup/', views.signup, name='signup'),
    path('test_csrf/', views.test_csrf, name='test_csrf'),  # New URL pattern for test CSRF page
]
