#Write a Python program that manipulates and prints strings using various string methods.
# Define a string
text = "  hello python programming  "

# Original string
print("Original String:", text)

# Remove leading and trailing spaces
print("After strip():", text.strip())

# Convert to uppercase
print("Uppercase:", text.upper())

# Convert to lowercase
print("Lowercase:", text.lower())

# Capitalize first letter
print("Capitalize:", text.capitalize())

# Replace word
print("Replace 'python' with 'Java':", text.replace("python", "Java"))

# Find position of a word
print("Position of 'python':", text.find("python"))

# Count occurrences of a letter
print("Count of 'o':", text.count("o"))

# Check if string starts with 'hello'
print("Starts with 'hello':", text.strip().startswith("hello"))

# Split the string into a list
print("Split string:", text.strip().split())
