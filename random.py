#Write a Python program to generate random numbers using the random module.
# Import random module

import random

print("Random number between 1 and 10:", random.randint(1, 10))
print("Random float between 0 and 1:", random.random())

numbers = [10, 20, 30, 40, 50]
print("Random choice from list:", random.choice(numbers))
