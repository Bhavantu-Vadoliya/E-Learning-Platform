from django.urls import path
from . import views

from . import views

urlpatterns = [
    path('dashboard/', views.student_dashboard, name='student_dashboard'),

    path('', views.index, name='indexpage'),
    path('Courses/', views.courses, name='courses'),
    path('About/', views.about, name='about'),
    path('Contact/', views.contact, name='contact'),
    path('signin/', views.signin, name='signin'),
    path('signup/', views.signup, name='signup'),
    path('test_csrf/', views.test_csrf, name='test_csrf'),  # New URL pattern for test CSRF page
]
