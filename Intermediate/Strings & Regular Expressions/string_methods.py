# Demonstrating common string methods

text = "  Hello, Python World!  "

# strip() - removes leading/trailing spaces
clean = text.strip()
print("After strip():", clean)

# split() - split into list by spaces
words = clean.split()
print("After split():", words)

# join() - join list into single string
joined = "-".join(words)
print("After join():", joined)

# replace() - replace substring
replaced = clean.replace("Python", "Coding")
print("After replace():", replaced)