
from typing import List
from collections import defaultdict


class Solution:
    def subarraySumEqualsK(self, nums: List[int], k: int) -> int:
        counts = defaultdict(int)
        ans = curr = 0
        counts[0] = 1
        for num in nums:
            curr += num
            ans += counts[curr - k]
            counts[curr] += 1
        
        return ans

results = Solution()
nums = [1,2,1,2,1]
k = 17
print(results.subarraySumEqualsK(nums, k))


