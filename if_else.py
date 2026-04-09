4#Conditional Statements
#Write a Python program to find greater and less than a number using
if_else

# Program to compare two numbers

# 1. Take input from the user
# The input() function gets a string, so we convert it to an integer using int()

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
print("Invalid input. Please enter only numbers.")
exit()

# 2. Compare the numbers using if-elif-else statements
if num1 > num2:
    print(f"The first number ({num1}) is greater than the second number ({num2}).")
elif num1 < num2:
    print(f"The first number ({num1}) is less than the second number ({num2}).")
else:
    print(f"The first number ({num1}) and the second number ({num2}) are equal.")

