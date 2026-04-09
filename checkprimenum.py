# Write a Python program to check if a number is prime using if_else
"""
Program: Check whether a number is prime or not
"""

# Taking input from user
num = int(input("Enter a number: "))

# Prime number logic
if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")
else:
    print(num, "is not a prime number")
