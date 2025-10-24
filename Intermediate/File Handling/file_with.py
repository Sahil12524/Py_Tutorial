# Automatically closes the file after the block ends

with open("notes.txt", "r") as f:
    data = f.read()
    print("Using with statement:\n", data)

# File is automatically closed outside the block
# No need to manually call close() — the best practice in Python.