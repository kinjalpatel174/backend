# Print this pattern using nested for loop: markdown Copy code 


"""
Program: Print star pattern using nested for loop
"""

# Outer loop for rows
for i in range(1, 6):
    
    # Inner loop for printing stars
    for j in range(i):
        print("*", end="")
    
    # Move to next line after each row
    print()
