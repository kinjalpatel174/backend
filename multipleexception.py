#Write a Python program to demonstrate handling multiple exceptions.

try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    result = a / b
    print("Result:", result)

except ZeroDivisionError:
    print("Error: You cannot divide by zero.")

except ValueError:
    print("Error: Please enter valid numbers.")

except Exception as e:
    print("Some other error occurred:", e)

finally:
    print("Program execution completed.")
