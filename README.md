# E-Learning Platform

## About
This project is a Django application designed to provide users with a platform for interacting with various features. It aims to facilitate learning and engagement through a user-friendly interface.

## Description
This project serves as a platform for users to interact with various features, including course management, user authentication, and dashboards for both students and teachers.

## Features
- **User Authentication**: Users can sign up, log in, and log out. The application supports different user types (students and teachers).
- **Course Management**: Teachers can create courses, and students can enroll in them. The application allows users to view all available courses and their enrollment status.
- **Dashboards**: Separate dashboards for students and teachers provide tailored experiences based on user type.
- **Contact Form**: Users can submit inquiries through a contact form.
- **Logging**: The application includes logging for various actions, aiding in debugging and monitoring.

## Frontend Technology
- **Tailwind CSS**: The project utilizes Tailwind CSS for styling, allowing for rapid UI development.

## Prerequisites
- Python 3.x
- Django 5.1.4
- Node.js (for frontend dependencies)

## Installation
1. **Create a virtual environment**:
   ```bash
   python -m venv venv
   ```
2. **Activate the virtual environment**:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```
3. **Install Python dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
4. **Install Node.js dependencies**:
   ```bash
   cd theme/static_src
   npm install
   ```

## Running the Application
1. **Run migrations**:
   ```bash
   python manage.py migrate
   ```
2. **Start the development server**:
   ```bash
   python manage.py runserver
   ```

## Usage
Access the application by navigating to `http://127.0.0.1:8000/` in your web browser.

## Contributing
Feel free to submit pull requests or open issues for any improvements or bugs.

## License
This project is licensed under the MIT License.
