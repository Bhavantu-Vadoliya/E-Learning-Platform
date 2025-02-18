import logging
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from aiutorapp.models import CustomUser, Course, Enrollment, Contact  # Import the Contact model
from django.http import HttpResponse  # Import HttpResponse for file downloads
from django.shortcuts import get_object_or_404  # Import get_object_or_404 for fetching course

# Set up logging
logger = logging.getLogger(__name__)

def index(request):
    logger.info(f"Request method: {request.method}, Path: {request.path}")
    all_courses = Course.objects.all()  # Fetch all courses
    return render(request, 'index.html', {'user': request.user, 'courses': all_courses})  # Pass user and courses context

def courses(request):
    logger.info(f"Request method: {request.method}, Path: {request.path}")
    all_courses = Course.objects.all()  # Fetch all courses
    enrolled_courses = Enrollment.objects.filter(student=request.user.id).values_list('course', flat=True) if request.user.is_authenticated else []  # Fetch enrolled course IDs for authenticated users

    return render(request, 'courses.html', {'courses': all_courses, 'enrolled_courses': enrolled_courses})

def enroll_course(request, course_id):
    logger.info(f"Request method: {request.method}, Path: {request.path}")
    if request.method == 'POST':
        course = Course.objects.get(id=course_id)
        # Check if the student is already enrolled
        if Enrollment.objects.filter(student=request.user, course=course).exists():
            logger.info(f"User {request.user.username} is already enrolled in course: {course.name}")
            return redirect('courses')  # Redirect to the courses page if already enrolled

        # Logic to enroll the student in the course
        Enrollment.objects.create(student=request.user, course=course)  # Save the enrollment

        logger.info(f"User {request.user.username} enrolled in course: {course.name}")
        return redirect('student_dashboard')  # Redirect to the courses page after enrollment

    return redirect('dashboard')  # Redirect to the dashboard for non-POST requests

def create_course(request):
    logger.info(f"Request method: {request.method}, Path: {request.path}")
    if request.method == 'POST':
        course_name = request.POST.get('course_name')
        description = request.POST.get('description')
        file = request.FILES.get('file')  # Get the uploaded file
        media_files = request.FILES.get('media_files')  # Get the uploaded media files
        youtube_link = request.POST.get('youtube_link')  # Get the YouTube link

        teacher = request.user  # Assuming the user is a teacher

        # Create a new course instance
        new_course = Course.objects.create(
            name=course_name,
            description=description,
            creator=teacher,  # Assuming there's a creator field in the Course model
            file=file,  # Save the uploaded file
            media_files=media_files,  # Save the uploaded media files
            youtube_link=youtube_link  # Save the YouTube link

        )
        new_course.save()
        logger.info(f"Course created: {new_course.name} by {teacher.username}")
        return redirect('courses')  # Redirect to the courses page after creation

    return render(request, 'teacher_dashboard.html')  # Render the dashboard for GET requests

from aiutorapp.models import Contact  # Import the Contact model

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        # Save the contact form data to the database
        contact_entry = Contact(name=name, email=email, message=message)
        contact_entry.save()  # Save the entry to the database
        
        logger.info(f"Contact form submitted by {name} ({email}): {message}")
        return redirect('indexpage')  # Redirect to a thank you page or the index page

    logger.info(f"Request method: {request.method}, Path: {request.path}")
    return render(request, 'contact.html')

def about(request):
    logger.info(f"Request method: {request.method}, Path: {request.path}")
    return render(request, 'about.html')

def privacy_policy(request):
    return render(request, 'privacy_policy.html')

def terms_of_service(request):
    return render(request, 'terms_of_service.html')

def student_dashboard(request):
    logger.info(f"Request method: {request.method}, Path: {request.path}")
    if request.user.is_authenticated and request.user.user_type == 'student':
        all_courses = Course.objects.all()  # Fetch all available courses
        enrolled_courses = Course.objects.filter(id__in=Enrollment.objects.filter(student=request.user).values_list('course', flat=True))  # Fetch enrolled course objects
        
        # # Pre-calculate enrollment status for each course
        # enrollment_status = {
        #     course.id: Enrollment.objects.filter(student=request.user, course=course).exists()
        #     for course in all_courses
        # }

        return render(request, 'dashboard.html', {
            'user': request.user,
            'enrolled_courses': enrolled_courses,
            'available_courses': all_courses,
        })  # Pass both to the template
    else:
        return redirect('indexpage')  # Redirect to index if not a student

def teacher_dashboard(request):
    logger.info(f"Request method: {request.method}, Path: {request.path}")
    if request.user.is_authenticated and request.user.user_type == 'teacher':
        created_courses = Course.objects.filter(creator=request.user)  # Fetch courses created by the teacher
        return render(request, 'teacher_dashboard.html', {'created_courses': created_courses})
    else:
        return redirect('indexpage')  # Redirect to index if not a teacher

from django.contrib.auth import logout

def logout_view(request):
    logout(request)
    return redirect('indexpage')  # Redirect to the index page after logout

def signin(request):
    logger.info(f"Request method: {request.method}, Path: {request.path}")
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)  # Log the user in
            logger.info(f"User {user.username} signed in successfully.")
            if user.user_type == 'student':
                return redirect('student_dashboard')  # Redirect to the student dashboard
            elif user.user_type == 'teacher':
                return redirect('teacher_dashboard')  # Redirect to the teacher dashboard
        else:
            logger.warning("Invalid credentials.")
            return render(request, 'signin.html', {'error': 'Invalid username or password.'})

    return render(request, 'signin.html')

def signup(request):
    logger.info(f"Request method: {request.method}, Path: {request.path}")
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user_type = request.POST.get('user_type')
        
        logger.info(f"Received data: Full Name: {full_name}, Email: {email}, User Type: {user_type}")
        
        if not email or not full_name or not password:
            logger.error("Error: Missing required fields")
            return render(request, 'signup.html')

        user = CustomUser.objects.create_user(
            username=email,
            email=email,
            password=password,
            first_name=full_name,
            user_type=user_type
        )
        user.save()
        logger.info(f"User created: {user.username}, User Type: {user.user_type}")
        
    return render(request, 'signup.html')
