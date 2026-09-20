# Student Management System

A web-based Student Management System developed using Django. The application provides a centralized platform for managing student information, courses, fees, examination results, and administrative operations.

## Features

- Student management
- Student registration and profile management
- Course management
- Fee management
- Result management
- Django Admin Panel
- Contact management
- Authentication and login functionality
- Database-driven student records
- Responsive web interface
- Static assets and media support

## Tech Stack

- **Backend:** Django 5.1.5
- **Programming Language:** Python
- **Database:** SQLite
- **Frontend:** HTML, CSS, JavaScript
- **Image Processing:** Pillow
- **Version Control:** Git & GitHub

## Project Structure

```text
Student-Management-System/
│
├── adminPanel/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── migrations/
│
├── front/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── migrations/
│
├── StudentManagement/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── static/
├── templates/
├── manage.py
├── requirements.txt
└── .gitignore
```

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/student-management-system.git
```

### 2. Open the project

```bash
cd student-management-system
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

#### Windows

```bash
venv\Scripts\activate
```

#### macOS/Linux

```bash
source venv/bin/activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Apply migrations

```bash
python manage.py migrate
```

### 7. Create a Django superuser

```bash
python manage.py createsuperuser
```

Follow the instructions in the terminal to create your own admin credentials.

### 8. Run the development server

```bash
python manage.py runserver
```

Open the application in your browser:

```text
http://127.0.0.1:8000/
```

## Admin Panel

The Django administration panel can be accessed through:

```text
http://127.0.0.1:8000/admin/
```

Use the superuser credentials created using:

```bash
python manage.py createsuperuser
```

## Database

The project uses SQLite for local development. Django migrations are included in the project to create and update the required database structure.

## Security

Sensitive information such as passwords, environment variables, local databases, virtual environments, and IDE-specific files should not be committed to the repository.

## Future Improvements

- Deploy the application to a cloud platform
- Add role-based authentication
- Add student attendance management
- Add email notifications
- Add analytics and reporting dashboards
- Improve API integration
- Add automated testing

## Author

**Piyush Kumar**

## License

This project is intended for educational and project-development purposes.
