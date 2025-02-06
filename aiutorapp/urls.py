from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='indexpage'),
    path('Courses/', views.courses, name='courses'),
    path('About/', views.about, name='about'),
    path('Contact/', views.contact, name='contact'),
    path('signin/', views.signin, name='signin'),
    path('signup/', views.signup, name='signup'),
]
