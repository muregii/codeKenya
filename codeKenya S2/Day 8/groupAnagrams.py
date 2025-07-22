from collections import defaultdict
from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #1. Time O(N.KlogK) 2. Space O(NK)
        
        groups = defaultdict(list) # O(1) 1. ordinary dictionary 2. defaultdict
        for s in strs: #O(n)
            key = ''.join(sorted(s)) # Timsort O(N.KlogK)
            groups[key].append(s) #O(1)

        return list(groups.values()) #O(n)
    