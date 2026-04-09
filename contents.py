 #Write a Python program to read the contents of a file and print them on the console

# Open the file in read mode
file = open("example.txt", "r")

# Read the contents of the file
content = file.read()

# Print the contents to the console
print(content)

# Close the file
file.close()
