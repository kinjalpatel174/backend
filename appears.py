# Write a Python program to count how many times each character appears in a string.
# Input string
text = input("Enter a string: ")

# Empty dictionary to store counts
char_count = {}

# Count characters
for ch in text:
    if ch in char_count:
        char_count[ch] += 1
    else:
        char_count[ch] = 1

# Print result
print("Character counts:")
for key, value in char_count.items():
    print(key, ":", value)
