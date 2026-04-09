#Write a Python program to create a class and access its properties using an object.

# Create a class
class Student:
    # Constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Create an object
s1 = Student("Kinjal", 20)

# Access properties using the object
print("Name:", s1.name)
print("Age:", s1.age)
