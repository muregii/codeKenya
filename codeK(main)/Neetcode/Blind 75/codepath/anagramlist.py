from typing import List
from collections import defaultdict
class Solution:
    def getAnagrams(self, lst: List[str]) -> List[List[str]]:
        map = defaultdict(list)
        for word in lst:
            #I wanna loop throuch each character
            # add to a hashmap and increase count by 1
            #if any key is more than the ||
            # yiu get the vibe, write the code
            char_count = [0] * 26
            for ch in word:
                char_count[ord(ch) - ord('a')] += 1
            key = tuple(char_count)
            map[key].append(word)
        return list(map.values())

s = Solution()
words = ["listen", "silent", "enlist", "google", "gooegl", "notanagram"]
result = s.getAnagrams(words)
print("Final grouped anagrams:")
print(result)


 
