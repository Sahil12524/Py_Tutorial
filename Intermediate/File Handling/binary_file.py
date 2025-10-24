# Writing and reading binary data

data = bytes([65, 66, 67, 68]) # A B C D in ASCII
with open("data.bin", "wb") as f:
    f.write(data)

with open("data.bin", "rb") as f:
    binary_data = f.read()
    print("Binary data:", binary_data)