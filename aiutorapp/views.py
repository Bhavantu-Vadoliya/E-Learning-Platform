import logging
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from aiutorapp.models import CustomUser

# Set up logging
logger = logging.getLogger(__name__)

def index(request):
    logger.info(f"Request method: {request.method}, Path: {request.path}")
    return render(request, 'index.html', {'user': request.user})  # Pass user context


def courses(request):
    logger.info(f"Request method: {request.method}, Path: {request.path}")
    return render(request, 'courses.html')

def contact(request):
    logger.info(f"Request method: {request.method}, Path: {request.path}")
    return render(request, 'contact.html')

def about(request):
    logger.info(f"Request method: {request.method}, Path: {request.path}")
    return render(request, 'about.html')

def student_dashboard(request):    
    # Check if the user is a student

    logger.info(f"Request method: {request.method}, Path: {request.path}")
    
    # Check if the user is a student
    if request.user.is_authenticated and request.user.user_type == 'student':
        return render(request, 'dashboard.html')
    else:
        return redirect('indexpage')  # Redirect to index if not a student


def teacher_dashboard(request):
    logger.info(f"Request method: {request.method}, Path: {request.path}")
    
    # Check if the user is a student
    if request.user.is_authenticated and request.user.user_type == 'teacher':
        return render(request, 'teacher_dashboard.html')
    else:
        return redirect('indexpage')  # Redirect to index if not a student


from django.contrib.auth import logout

def logout_view(request):
    logout(request)
    return redirect('indexpage')  # Redirect to the index page after logout


def signin(request):


    logger.info(f"Request method: {request.method}, Path: {request.path}")
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        # Authenticate the user
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

    logger.info(f"Request method: {request.method}, Path: {request.path}")
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        # Authenticate the user
        user = authenticate(request, username=email, password=password)
        
        if user is not None:
            login(request, user)  # Log the user in
            logger.info(f"User {user.username} signed in successfully.")
            return redirect('../')  # Redirect to the index page
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
        
        # Create a new user instance
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

    logger.info(f"Request method: {request.method}, Path: {request.path}")
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user_type = request.POST.get('user_type')
        
        logger.info(f"Received data: Full Name: {full_name}, Email: {email}, User Type: {user_type}")
        
        # Create a new user instance
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

    return render(request, 'signup.html')

def test_csrf(request):
    logger.info(f"Request method: {request.method}, Path: {request.path}")
