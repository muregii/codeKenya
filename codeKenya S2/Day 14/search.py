"""Searching algorithms.

1. for loop: linear search
2. Binary Search
3. DFS/BFS 
4. Backtrack

 """
# binary search  c A - Jersey Z
#[1, 2, 3 ,4, 5] _ 4//2 = 2
#[1,2] [3] [4,5]
#is 3 == 4? No
# if 3 > or < 4?
#[4,5]
#[4] [5]
#is 4 == 4 ? Yes
#return 4, indice 3

#arr = [8,7,6,5,4,3,2,9] # t =  2 
#sorted_arr = [2,3,4,5,6,7,8,9]
##7 // 2 = 3

from typing import List
class Solution:
    def binary_search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1

        while left <= right:
            mid = (left + right) // 2

            if target < nums[mid]:
                right = mid -1
            elif target > nums[mid]:
                left = mid + 1
            else:
                return mid
        return -1

sorted_arr = [2,3,4,5,6,7,8,9]
target = 2
result = Solution().binary_search(sorted_arr, target)
print(result)
        



      





