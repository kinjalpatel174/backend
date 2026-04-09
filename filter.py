#Write a Python program that filters out even numbers using the filter() function.

# Define a list of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8]

# Use filter() to get even numbers
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

# Print the result
print("Original List:", numbers)
print("Even Numbers:", even_numbers)
