#Write a Python program to search for a word in a string using re.search().
import re

# Input string
text = "Python programming is easy and fun"

# Word to search
word = "easy"

# Use re.search() to find the word
match = re.search(word, text)

if match:
    print(f"'{word}' found in the string!")
else:
    print(f"'{word}' not found in the string.")
