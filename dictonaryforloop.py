# Write a Python program to convert two lists into one dictionary using a for loop. 
# First list (keys)
keys = ["id", "name", "age", "course"]

# Second list (values)
values = [101, "Amit", 21, "Python"]

# Empty dictionary
my_dict = {}

# Using for loop to combine lists
for i in range(len(keys)):
    my_dict[keys[i]] = values[i]

# Print dictionary
print("Resulting Dictionary:", my_dict)
