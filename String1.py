#Write a Python program to match a word in a string using re.match().

import re

text = "Python programming is fun"
word = "Python"

match = re.match(word, text)

if match:
    print(f"'{word}' matches at the beginning of the string!")
else:
    print(f"'{word}' does NOT match at the beginning of the string.")
