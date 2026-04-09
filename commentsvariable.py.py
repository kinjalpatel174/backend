#2. Programming Style
# Write a Python program that demonstrates the correct use of indentation, comments, and variablesfollowing PEP 8 guidelines.

##Here is simple Python program that demonstrates:

#1 Proper indentation (4 spaces)

#2 Meaningful variable names

#3 Proper comments

#4 Clean formatting following PEP 8 guidelines

"""
Program: Student Grade Calculator
Description: Demonstrates proper indentation, comments,
             and variable naming according to PEP 8.
"""

# Store student details in variables
student_name = "Kinjal"
marks_math = 85
marks_science = 90
marks_english = 88

# Calculate total marks
total_marks = marks_math + marks_science + marks_english

# Calculate average marks
average_marks = total_marks / 3

# Display results
print("Student Name:", student_name)
print("Total Marks:", total_marks)
print("Average Marks:", average_marks)

# Check grade using proper indentation
if average_marks >= 90:
    grade = "A+"
elif average_marks >= 80:
    grade = "A"
elif average_marks >= 70:
    grade = "B"
else:
    grade = "C"

print("Grade:", grade)


#Why This Follows PEP 8:

#1. four spaces used for indentation

#2. Variable names use lowercase with underscores (student_name)

#3. Meaningful variable names

#4  Comments explain each section clearly

#5. Proper spacing around operators (=, +, /)

#6. Blank lines used to separate logical sections
