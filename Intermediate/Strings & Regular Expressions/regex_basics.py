# Regular Expressions in Python

import re

text = "Hello 123 world_42! Python is cool 999 times."

# \d – any digit
print(re.findall(r"\d", text))        # → ['1', '2', '3', '4', '2', '9', '9', '9']

# \w – any word character (letters, digits, underscore)
print(re.findall(r"\w+", text))       # → ['Hello', '123', 'world_42', 'Python', 'is', 'cool', '999', 'times']

# \s – whitespace characters
print(re.findall(r"\s", text))        # → [' ', ' ', ' ', ' ', ' ', ' ', ' ']

# ^ – start of string
print(bool(re.match(r"^Hello", text)))  # → True

# $ – end of string
print(bool(re.search(r"times\.$", text)))  # → True

# . – any single character except newline
print(re.findall(r"P.thon", text))    # → ['Python']

# * – zero or more occurrences
print(re.findall(r"\d*", text))       # → matches all digit sequences, including empty ones

# + – one or more occurrences
print(re.findall(r"\d+", text))       # → ['123', '42', '999']

# ? – zero or one occurrence (optional)
print(re.findall(r"cool?", text))     # → ['cool']

# {n} – exactly n occurrences
print(re.findall(r"\d{3}", text))     # → ['123', '999']

# {m,n} – between m and n occurrences
print(re.findall(r"\d{2,3}", text))   # → ['123', '42', '999']

# | – OR condition
print(re.findall(r"Python|Java", text))   # → ['Python']

# () – grouping
print(re.findall(r"(world)_(\d+)", text)) # → [('world', '42')]

# \b – word boundary
print(re.findall(r"\bPython\b", text))    # → ['Python']

# Split using regex (split by spaces or punctuation)
print(re.split(r"[\s!]+", text))          # → ['Hello', '123', 'world_42', 'Python', 'is', 'cool', '999', 'times.']

# Replace digits with X
print(re.sub(r"\d", "X", text))           # → 'Hello XXX world_XX! Python is cool XXX times.'