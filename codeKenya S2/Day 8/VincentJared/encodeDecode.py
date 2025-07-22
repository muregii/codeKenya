"""Design an algorithm to encode a list of strings to a single string.
The encoded string is then decoded back to the original list of strings."""
from typing import List
class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        ans = ""
        for s in strs:
            ans += str(len(s)) + "#" + s
            
        return s
        
    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        ans, l = [], 0
        while l < len(s):
            j = l
            while s[j]!="#":
                j+=1
            length =  int(s[l:j])
            ans.append(s[j +1:j + 1 + length])
            l = j + 1+ length
            
        return s

print(Codec().encode(["Hello", "World"]))
print(Codec().decode("5#Hello5#World"))
print(Codec().encode(["", ""]))
print(Codec().decode("0#0#"))
print(Codec().encode(["a", "b", "c"]))
print(Codec().decode("1#a1#b1#c")) 

   
        