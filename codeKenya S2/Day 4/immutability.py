s = "hello"
print(id(s), s)   # e.g. 140222631488848, "hello"

# Trying to mutate a character raises an error
try:
    s[0] = "H"
except TypeError as e:
    print("Error")
# → Error: 'str' object does not support item assignment

# “Modifying” a string actually creates a new one
t = "H" + s[1:]
print(id(s), s)   # original unchanged
print(id(t), t)