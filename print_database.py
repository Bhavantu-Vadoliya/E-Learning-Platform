import os
import django
from django.conf import settings

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'aiutor.settings')
django.setup()

from aiutorapp.models import CustomUser, Course, Enrollment, Contact


def print_database():
    print("CustomUser:")
    for user in CustomUser.objects.all():
        designation = user.user_type  # Get the designation
        print(f"{user.username} - {designation}")  # Print username with designation

    print("\nCourse:")
    for course in Course.objects.all():
        print(course)

    print("\nEnrollment:")
    for enrollment in Enrollment.objects.all():
        print(enrollment)

    print("\nContact:")
    for contact in Contact.objects.all():
        print(contact)

if __name__ == "__main__":
    print_database()
