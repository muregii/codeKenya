from typing import List
from collections import defaultdict
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        #Make the dictionary
        for num in nums:
            freq[num] += 1


        heap = []
        # Create a max heap
        for key, val in freq.items():
            heapq.heappush(heap, (-val, key))

        ans = []
        # from the heap, get the element in the first index.
        for _ in range(k):
            ans.append(heapq.heappop(heap)[1])

        return ans
# Example usage
print(Solution().topKFrequent([1, 1, 1, 2, 2, 3], 2))
# Time complexity: O(n) for building the frequency dictionary
# O(n log K) for building the heap
# Space complexity: O(n) for the frequency dictionary and heap
# O(k) for the result list
# Overall time complexity: O(n + n log K) = O(n log K)
# Overall space complexity: O(n + k) = O(n) if k is small compared to n
