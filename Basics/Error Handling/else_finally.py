# Using else and finally with try-except

try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ZeroDivisionError:
    print("Error: You cannot divide by zero.")
else:
    print("Division successful! Result =", result)
finally:
    print("This message always runs - cleanup done.")