# Break, Continue, and Else in Loops

# Using break
for i in range(10):
    if i == 5:
        print("Breaking at 5.")
        break
    print(i)
print("Loop ended.")

print("-" * 20)

# Using continue
for i in range(5):
    if i == 2:
        continue
    print("Value:", i)

print("-" * 20)

# Using else with loop
for i in range(3):
    print(i)
else:
    print("Loop completed successfully (no break).")

print("-" * 20)

# Example with break that skips else
for i in range(5):
    if i == 3:
        break
    print(i)
else:
    print("This will NOT print because of break.")