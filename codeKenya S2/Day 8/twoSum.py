from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #1. Time O(n) 2. Space O(n)
        map = {}
        for index, num in enumerate(nums):
            complement = target - num
            if complement in map:
                return(map[complement], index)
            map[num] = index
        return -1

    #1. Time O(n^2)  2. Space O(1)
    def twoSum2(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n):
            for j in range(1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return -1




       

        