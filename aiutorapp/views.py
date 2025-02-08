import logging
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from aiutorapp.models import CustomUser, Course, Enrollment  # Assuming Course is the model for courses

# Set up logging
logger = logging.getLogger(__name__)

def index(request):
    logger.info(f"Request method: {request.method}, Path: {request.path}")
    return render(request, 'index.html', {'user': request.user})  # Pass user context

def courses(request):
    logger.info(f"Request method: {request.method}, Path: {request.path}")
    all_courses = Course.objects.all()  # Fetch all courses
    return render(request, 'courses.html', {'courses': all_courses})

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
        teacher = request.user  # Assuming the user is a teacher

        # Create a new course instance
        new_course = Course.objects.create(
            name=course_name,
            description=description,
            creator=teacher  # Assuming there's a creator field in the Course model
        )
        new_course.save()
        logger.info(f"Course created: {new_course.name} by {teacher.username}")
        return redirect('courses')  # Redirect to the courses page after creation

    return render(request, 'teacher_dashboard.html')  # Render the dashboard for GET requests

def contact(request):
    logger.info(f"Request method: {request.method}, Path: {request.path}")
    return render(request, 'contact.html')

def about(request):
    logger.info(f"Request method: {request.method}, Path: {request.path}")
    return render(request, 'about.html')

def student_dashboard(request):    
    logger.info(f"Request method: {request.method}, Path: {request.path}")
    if request.user.is_authenticated and request.user.user_type == 'student':
        all_courses = Course.objects.all()  # Fetch all available courses
        enrolled_courses = Enrollment.objects.filter(student=request.user).select_related('course')  # Fetch enrolled courses
        return render(request, 'dashboard.html', {
            'available_courses': all_courses,
            'enrolled_courses': enrolled_courses
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
        
        return redirect('signin')  # Redirect to the signin page after successful signup

    return render(request, 'signup.html')

def test_csrf(request):
    logger.info(f"Request method: {request.method}, Path: {request.path}")
