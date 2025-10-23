# Take user input
name = input("Enter your name: ")
age = int(input("Enter your age: "))

# Display output
print(f"Hello {name}! You are {age} years old.")

# Perform a calculation
next_year_age = age + 1
print(f"Next year, you will be {next_year_age}.")

# Print with custom separator and end
print("Python", "is", "awesome", sep="-", end="!\n")