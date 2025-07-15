from collections import Counter

class Solution:
    #1. Time O(n log n)    2. Space O(n)
    def isAnagram3(self, s: str, t: str):
        return sorted(s) == sorted(t)
    #1. Time O(n)    2. Space O(k)
    def isAnagram2(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
    #1. Time O(n)    2. Space O(1) -> MOST OPTIMAL
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        counts= [0] * 26 # Space O(1)
        base = ord('a')

        for char in s:
            counts[ord(char) - base] +=1 

        for char in t:
            counts[ord(char) - base] -=1 
            if counts[ord(char) - base] <0:
                return False

        return True

print(Solution().isAnagram3("rat", "tar"))
    


        

        