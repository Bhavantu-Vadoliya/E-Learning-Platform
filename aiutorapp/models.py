from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
        ('teacher', 'As Teacher'),
        ('student', 'As Student'),
    )
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES)

class Course(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    creator = models.ForeignKey(CustomUser, on_delete=models.CASCADE)  # Link to the teacher who created the course
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp for when the course was created

    def __str__(self):
        return self.name

class Enrollment(models.Model):
    student = models.ForeignKey(CustomUser, on_delete=models.CASCADE)  # Link to the student
    course = models.ForeignKey(Course, on_delete=models.CASCADE)  # Link to the course
    enrolled_at = models.DateTimeField(auto_now_add=True)  # Timestamp for when the enrollment occurred

    def __str__(self):
        return f"{self.student.username} enrolled in {self.course.name}"
