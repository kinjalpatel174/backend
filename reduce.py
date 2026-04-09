#Write a Python program that uses reduce() to find the product of a list of numbers.

from functools import reduce

# Define a list of numbers
numbers = [1, 2, 3, 4, 5]

# Use reduce() to calculate the product
product = reduce(lambda x, y: x * y, numbers)

# Print the result
print("List of numbers:", numbers)
print("Product of numbers:", product)
