import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'edutracker.settings')
django.setup()

from core.models import Student, Course
from datetime import date

def seed():
    # Create Courses
    c1, _ = Course.objects.get_or_create(
        code='PY101',
        title='Python Basics',
        description='Learn the fundamentals of Python programming.'
    )
    c2, _ = Course.objects.get_or_create(
        code='DRF202',
        title='Django REST Framework',
        description='Master building RESTful APIs with Django.'
    )
    
    # Create Students
    s1, _ = Student.objects.get_or_create(
        email='john.doe@example.com',
        defaults={
            'first_name': 'John',
            'last_name': 'Doe',
            'dob': date(2000, 1, 1)
        }
    )
    s1.courses.add(c1, c2)
    
    s2, _ = Student.objects.get_or_create(
        email='jane.smith@example.com',
        defaults={
            'first_name': 'Jane',
            'last_name': 'Smith',
            'dob': date(2001, 5, 15)
        }
    )
    s2.courses.add(c1)
    
    print("Database seeded successfully!")

if __name__ == '__main__':
    seed()
