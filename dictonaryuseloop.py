#Write a Python program to merge two lists into one dictionary using a loop.

# First list (keys)
keys = ["id", "name", "age", "course"]

# Second list (values)
values = [101, "kinjal", 20, "Python"]

# Empty dictionary
result = {}

# Using loop to merge lists
for i in range(len(keys)):
    result[keys[i]] = values[i]

# Print dictionary
print("Merged Dictionary:", result)
