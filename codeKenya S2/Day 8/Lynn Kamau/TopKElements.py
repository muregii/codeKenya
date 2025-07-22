#Top K Frequent Elements Leetcode Challenge
#Given an integer array nums and an integer k, return the k most frequent elements. 
#You may return the answer in any order.

from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = {}
        for num in nums:
            if num in freq_map:
                freq_map[num] += 1
            else:
                freq_map[num] = 1
        sorted_items = sorted(freq_map.items(), key=lambda x: x[1], reverse=True)
        result = [item[0] for item in sorted_items[:k]]
        return result

#Test Cases
if __name__ == "__main__":
    solution = Solution()
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    print("Top", k, "frequent elements:", solution.topKFrequent(nums, k)) 
    nums = [1]
    k = 1
    print("Top", k, "frequent elements:", solution.topKFrequent(nums, k)) 
    nums = [5,5,5,3,3,3,4,4,4,7,7,7,8,8,8]
    k = 2
    print("Top", k, "frequent elements:", solution.topKFrequent(nums, k)) 
