# Tuples in Python (Immutable)

numbers = (10, 20, 30, 40)

# Accessing elements
print("First number:", numbers[0])

# Iterating over tuple
for num in numbers:
    print("Number:", num)

# Trying to modify (will cause error if uncommented)
# numbers[0] = 99   #   TypeError

# Tuple unpacking
a, b, c, d = numbers
print("Unpacked values:", a, b, c, d)

# Useful functions
print("Length:", len(numbers))
print("Max:", max(numbers))
print("Min:", min(numbers))