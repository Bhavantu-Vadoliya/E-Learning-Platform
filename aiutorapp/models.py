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
    file = models.FileField(upload_to='course_files/', blank=True, null=True)  # Field for uploading course files
    media_files = models.FileField(upload_to='media_files/', blank=True, null=True)  # Field for uploading multiple media files
    youtube_link = models.URLField(blank=True, null=True)  # Field for storing YouTube video link



    def __str__(self):
        return f"{self.creator.username}  in {self.name}"

class Enrollment(models.Model):
    student = models.ForeignKey(CustomUser, on_delete=models.CASCADE)  # Link to the student
    course = models.ForeignKey(Course, on_delete=models.CASCADE)  # Link to the course
    enrolled_at = models.DateTimeField(auto_now_add=True)  # Timestamp for when the enrollment occurred

    def __str__(self):
        return f"{self.student.username} enrolled in {self.course.name}"
    def is_enrolled(self, course):
        return Enrollment.objects.filter(student=self, course=course).exists()

class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
