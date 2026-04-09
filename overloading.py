#Write Python programs to demonstrate method overloading and method overriding
class Calculator:
    # Method with default arguments simulates overloading
    def add(self, a, b=0, c=0):
        result = a + b + c
        print("Sum =", result)

# Create object
calc = Calculator()

# Different number of arguments
calc.add(5)          # One argument
calc.add(5, 10)      # Two arguments
calc.add(5, 10, 15)  # Three arguments
