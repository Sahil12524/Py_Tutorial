# Sets in Python (Unordered & Unique)

nums = {1, 2, 3, 3, 4, 5}
print("Set:", nums) # Duplicates removed

# Adding and removing
nums.add(6)
print("After add:", nums)

nums.remove(3)
print("After remove:", nums)

# Set operations
a = {1, 2, 3}
b = {3, 4, 5}

print("Union:", a | b)
print("Intersection:", a & b)
print("Difference:", a - b)
print("Symmetric Difference:", a ^ b)

# Membership
print("2 in a:", 2 in a)