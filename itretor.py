#Write a Python program that uses a custom iterator to iterate over a list of integers.
# Custom Iterator Class
class MyIterator:
    def __init__(self, data):
        self.data = data      # Store the list
        self.index = 0        # Start index

    def __iter__(self):
        return self          # Return the iterator object itself

    def __next__(self):
        if self.index < len(self.data):
            value = self.data[self.index]
            self.index += 1
            return value
        else:
            raise StopIteration   # Stop when list ends


# List of integers
numbers = [10, 20, 30, 40, 50]

# Create iterator object
my_iter = MyIterator(numbers)

# Iterate using for loop
print("Iterating using custom iterator:")
for num in my_iter:
    print(num)
