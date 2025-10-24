# f-strings are the modern way to format text

name = "Sahil"
age = 22
score = 95.6789

# f-string
print(f"My name is {name}, age {age}, score {score:.2f}")

# .format() method (older style)
print("My name is {}, age {}, score {:.2f}".format(name, age, score))

# % formatting (legacy)
print("My name is %s, age %d, score %.2f" % (name, age, score))

# Best Practice: Use f-strings for readability and performance.