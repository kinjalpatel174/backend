#Practical Example 3: How to take user input using the input() function


#Important: input() always returns the value as a string.

#Basic Example (String Input)
name = input("Enter your name: ")
print("Hello,", name)

#Taking Integer Input
#Since input()Returns a string, convert it using int():
age = int(input("Enter your age: "))
print("Your age is:", age)

#Taking Float Input
height = float(input("Enter your height: "))
print("Your height is:", height)

#Taking Multiple Inputs
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("Sum is:", num1 + num2)






