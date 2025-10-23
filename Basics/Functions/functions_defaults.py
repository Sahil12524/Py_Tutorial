# Default and Keyword Arguments

def describe_person(name, age = 18, city = "Unknown"):
    print(f"Name: {name}, Age: {age}, City: {city}")

# Using positional and default
describe_person("Sahil")

# Using keyword arguments
describe_person(name = "Pooja", city = "Mumbai", age = 19)

# Mix of both
describe_person("Aishu", city = "Mumbai")