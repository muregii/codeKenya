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

    # O(n) space
    # O(n log K) time complexity
        