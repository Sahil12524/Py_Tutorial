# Basic try-except example

try:
    num = int(input("Enter a number: "))
    print("10 divide by your number is:", 10 / num)
except:
    print("Something went wrong!") # Generic Catch for any error