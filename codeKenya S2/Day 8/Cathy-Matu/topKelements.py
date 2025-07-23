#Using the bucket sort technique to
#count the frequency of each element using  a hash map
#Group elements to buckets based on their frequency
#Iterate from the highest frequency down, collecting elements until k elements are found
from collections import defaultdict
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Count the frequency of each number
        freq_map = defaultdict(int)
        for num in nums:
            freq_map[num] += 1
        
        # Step 2: Create buckets where index = frequency
        buckets = [[] for _ in range(len(nums) + 1)]
        for num, freq in freq_map.items():
            buckets[freq].append(num)
        
        # Step 3: Collect top k frequent elements starting from highest freq
        res = []
        for freq in range(len(buckets) - 1, 0, -1):  # from high to low frequency
            for num in buckets[freq]:
                res.append(num)
                if len(res) == k:
                    return res

sol = Solution()
print(sol.topKFrequent([1, 2, 2, 3, 3, 3], 2))  
print(sol.topKFrequent([7, 7], 1))             
