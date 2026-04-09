#Write a Python program to find a specific string in the list using a simple
#for loop and if condition.

"""
Program: Search for a specific string in a list
"""

# Given list
List1 = ['apple', 'banana', 'mango']

# Taking input from user
search_item = input("Enter the fruit to search: ")

# Flag variable
found = False

# Using for loop and if condition
for fruit in List1:
    if fruit == search_item:
        found = True
        break

# Display result
if found:
    print(search_item, "is found in the list.")
else:
    print(search_item, "is not found in the list.")
