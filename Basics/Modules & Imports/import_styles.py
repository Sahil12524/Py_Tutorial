# Demonstrating different import styles

# Full module import
import math
print("Pi value:", math.pi)

# Import with alias
import math as m
print("Square root of 16:", m.sqrt(16))

# Import specific functions
from math import factorial, pow
print("5! =", factorial(5))
print("2^5 =", pow(2, 5))

# Import everything (not recommended)
from math import *
print("Cos(0):", cos(0))