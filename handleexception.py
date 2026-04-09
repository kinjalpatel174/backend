
#Write a Python program to handle exceptions in a simple calculator (division by zero, invalid input


try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    result = num1 / num2

    print("Result:", result)

except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

except ValueError:
    print("Error: Invalid input. Please enter numbers only.")

finally:
    print("Program finished.")
