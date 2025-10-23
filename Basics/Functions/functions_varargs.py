# Variable-Length Arguments (*args and **kwargs)

# *args -> collects positional arguments into a tuple
def add_all(*numbers):
    print("Numbers received:", numbers)
    total = sum(numbers)
    return total

print("Sum:", add_all(2, 4, 6, 8))

# **kwargs -> collects keyword arguments into a dictionary
def show_info(**info):
    print("Details:")
    for key, value in info.items():
        print(f"{key}: {value}")

show_info(name = "Sahil", age = 22, course = "Python", country = "India")