# Generators and Iterators
#Write a generator function that generates the first 10 even numbers.
def first_ten_even_numbers():
    """
    Generates the first 10 even numbers starting from 0.
    """
    count = 0
    num = 0
    while count < 10:
        yield num
        num += 2
        count += 1

# Example usage:
generator_object = first_ten_even_numbers()

# Iterate over the generator to get the numbers
for even_num in generator_object:
    print(even_num)

# Alternatively, convert to a list
even_numbers_list = list(first_ten_even_numbers())
print(even_numbers_list)
