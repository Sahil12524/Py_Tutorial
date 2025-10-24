# 'a' mode appends to the end of a file

file = open("notes.txt", "a")
file.write("Appending a new line!\n")
file.close()

# Reading back
with open("notes.txt", "r") as f:
    print(f.read())