# Integer
age = 23

# Float
height = 5.9

# String
name = "Sahil"

# Boolean
is_student = True

#NoneType
data = None

print(f"Name: {name}, Age: {age}, Height: {height}, Student: {is_student}")

print("Type of age: ", type(age))
print("Type of height: ", type(height))
print("Type of name: ", type(name))
print("Type of is_student: ", type(is_student))
print("Type of data: ", type(data))

# Dynamic typing demonstration
x = 10
print("Before: ", x, type(x))
x = "Now I'm a string"
print("After: ", x, type(x))