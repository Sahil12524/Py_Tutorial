# List, Set, and Dictionary Comprehensions

# List comprehension
squares = [x * x for x in range(6)]
print("Squares:", squares)

# With condition
even_squares = [x * x for x in range(10) if x % 2 == 0]
print("Even squares:", even_squares)

# Set comprehension
unique_lengths = {len(word) for word in ["apple", "banana", "pear"]}
print("Unique lengths:", unique_lengths)

# Dict comprehension
num_dict = {x: x**2 for x in range(5)}
print("Number squares dict:", num_dict)