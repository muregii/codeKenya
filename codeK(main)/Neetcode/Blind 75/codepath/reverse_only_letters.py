"""Problem 3: Reverse Letters
# Write a function reverse_only_letters() that takes in a string s as a parameter. 
# The function reverses the order of the letters in the string and returns the new 
# string. Non-letter characters should remain in their original positions."""

def reverse_letters(s):
    list_s = list(s)
    i, j = 0, len(s) - 1

    while i < j:
        list_s[i], list_s[j] = list_s[j], list_s[i]
        i+=1
        j-=1
    return "".join(list_s)

s = "raydon"
reversed_s = reverse_letters(s)
print(reversed_s)