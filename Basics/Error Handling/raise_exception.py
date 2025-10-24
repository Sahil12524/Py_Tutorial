# Raising a custom exception

def withdraw(balance, amount):
    if amount > balance:
        raise ValueError("Insufficient balance!") # Custom exception
    return balance - amount

try:
    new_balance = withdraw(1000, 1500)
    print("Remaining balance:", new_balance)
except ValueError as e:
    print("Error:", e)