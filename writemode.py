#Write a Python program to open a file in write mode, write some text, and then close it.

# Open file in write mode
file = open("example.txt", "w")

# Write text to the file
file.write("Hello, this is my first file in Python.\n")
file.write("Python file handling is easy to learn.")

# Close the file
file.close()

print("Data written successfully.")
