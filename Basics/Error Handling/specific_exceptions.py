# Catching specific exceptions

try:
    num = int(input("Enter a number: "))
    print("10 divided by your number is:", 10 / num)
except ValueError:
    print("Error: Please enter a valid integer.")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed!")