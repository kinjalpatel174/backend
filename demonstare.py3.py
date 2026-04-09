#Write a Python program to demonstrate the creation of variables and different data types


"""
Program: Demonstration of Variables and Data Types
Description: Shows how to create variables of different data types in Python.
"""

# Integer
age = 20

# Float
height = 5.6

# String
name = "Kinjal Patel"

# Boolean
is_student = True

# List
subjects = ["Math", "Science", "English"]

# Tuple
marks = (85, 90, 88)

# Dictionary
student_info = {
    "name": "Kinjal Patel",
    "age": 20,
    "course": "BCA"
}

# Set
unique_numbers = {1, 2, 3, 4, 5}

# Printing values and their data types
print("Name:", name, "| Type:", type(name))
print("Age:", age, "| Type:", type(age))
print("Height:", height, "| Type:", type(height))
print("Is Student:", is_student, "| Type:", type(is_student))
print("Subjects:", subjects, "| Type:", type(subjects))
print("Marks:", marks, "| Type:", type(marks))
print("Student Info:", student_info, "| Type:", type(student_info))
print("Unique Numbers:", unique_numbers, "| Type:", type(unique_numbers))

