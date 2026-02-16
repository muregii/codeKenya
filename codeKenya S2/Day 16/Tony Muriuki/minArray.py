from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            # Minimum is in right half
            if nums[mid] > nums[right]:
                left = mid + 1
            else:  
                # Minimum is in left half (including mid)
                right = mid

        return nums[left]
