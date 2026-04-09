# Practical Example 4: How to check the type of a variable dynamically using type()
"""
Program: Demonstrating use of type() function
"""
#Checking Different Variable Types
# Creating variables
name = "Kinjal"
age = 20
height = 5.4
is_student = True

# Checking types dynamically
print("Type of name:", type(name))
print("Type of age:", type(age))
print("Type of height:", type(height))
print("Type of is_student:", type(is_student))

#Example 2: Dynamic Type Change
x = 10
print("Value:", x, "Type:", type(x))

x = "Hello"
print("Value:", x, "Type:", type(x))

#Example 3: Using type() with User Input
user_input = input("Enter something: ")
print("You entered:", user_input)
print("Type is:", type(user_input))

#Since input() returns string, output type will always be:<class 'str'>

