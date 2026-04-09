# Write a Python program to calculate grades based on percentage using
#if-else ladder.
"""
Program: Calculate grade based on percentage
"""

# Taking percentage input from user
percentage = float(input("Enter your percentage: "))

# Grade calculation using if-else ladder
if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
elif percentage >= 35:
    grade = "E"
else:
    grade = "Fail"

# Display result
print("Your Grade is:", grade)
