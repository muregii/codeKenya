#Assignment six: String Encode and Decode Leetcode Challenge
#Design an algorithm to encode a list of strings to a single string.
#The encoded string is then sent over the network and is decoded back to the original list of strings. 
#Implement the encode and decode methods.

from typing import List

def encode(strs: List[str]) -> str:
    encoded = ""
    for s in strs:
        encoded += str(len(s)) + "#" + s
    return encoded

def decode(s: str) -> List[str]:
    decoded = []
    i = 0
    while i < len(s):
        j = i
        while s[j] != '#':
            j += 1
        length = int(s[i:j])
        word = s[j + 1: j + 1 + length]
        decoded.append(word)
        i = j + 1 + length
    return decoded

#Example usage
original = ["neet", "code", "love", "you"]
encoded_str = encode(original)
decoded_list = decode(encoded_str)

print("Original:", original)
print("Encoded:", encoded_str)
print("Decoded:", decoded_list)
