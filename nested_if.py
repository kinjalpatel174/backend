#Write a Python program to check if a person is eligible to donate blood using a nested if

"""
Program: Check blood donation eligibility using nested if
"""

# Taking input from user
age = int(input("Enter your age: "))
weight = float(input("Enter your weight (kg): "))
hemoglobin = float(input("Enter your hemoglobin level: "))

# Checking eligibility using nested if
if age >= 18 and age <= 60:
    if weight >= 50:
        if hemoglobin >= 12.5:
            print("You are eligible to donate blood.")
        else:
            print("You are not eligible due to low hemoglobin.")
    else:
        print("You are not eligible due to low weight.")
else:
    print("You are not eligible due to age criteria.")
