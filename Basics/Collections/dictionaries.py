# Dictionaries in Python (Key-Value pairs)

student = {
    "name": "Sahil",
    "age": 22,
    "course": "Python"
}

# Accessing
print("Name:", student["name"])
print("Course:", student.get("course"))

# Adding or updating
student["city"] = "Mumbai"
print("After adding city:", student)

# Iterating through keys and values
for key, value in student.items():
    print(f"{key}: {value}")

# Deleting
del student["age"]
print("After delete:", student)

# Checking keys
print("name" in student)