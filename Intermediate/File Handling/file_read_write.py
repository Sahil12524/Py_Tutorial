# Opening and writing to a text file

# 'w' mode overwrites existing content
file = open("notes.txt", "w")
file.write("Hello, python!\n")
file.write("Learning file handling.\n")
file.close()

# Reading the file content
file = open("notes.txt", "r")
content = file.read()
print("File content:\n", content)
file.close()