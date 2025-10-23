# Conditional Statements in Python

num = int(input("Enter a number: "))

if num > 0:
    print("Positive number.")
elif num == 0:
    print("Number is zero.")
else:
    print("Negative number.")

# Nested if example
age = int(input("Enter your age: "))
if age >= 18:
    if age < 60:
        print("Your are an adult.")
    else:
        print("You are a senior citizen.")
else:
    print("You are a minor.")