from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
        ('teacher', 'As Teacher'),
        ('student', 'As Student'),
    )
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES)

# Ensure to update the settings.py to use this custom user model
