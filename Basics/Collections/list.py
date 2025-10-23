# List in Python

# Creating a list
fruits = ["apple", "banana", "cherry"]
print("Fruits:", fruits)

# Accessing elements
print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])

# Adding elements
fruits.append("mango")
print("After append:", fruits)

# Inserting at specific position
fruits.insert(1, "orange")
print("After insert:", fruits)

# Removing elements
fruits.remove("banana")
print("After remove:", fruits)

# Popping last element
last = fruits.pop()
print("Popped:", last)
print("After pop:", fruits)

# Iterating through list
for fruit in fruits:
    print("Fruit:", fruit)

# Checking membership
print("apple" in fruits)