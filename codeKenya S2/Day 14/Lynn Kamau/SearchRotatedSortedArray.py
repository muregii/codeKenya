#Search in Rotated Sorted Array Leetcode Problem
#You are given an array of length n which was originally sorted in ascending order. It has now been rotated between 1 and n times. 
# For example, the array nums = [1,2,3,4,5,6] might become:[3,4,5,6,1,2] if it was rotated 4 times. [1,2,3,4,5,6] if it was rotated 6 times.
# Given the rotated sorted array nums and an integer target, return the index of target within nums, or -1 if it is not present.
# You may assume all elements in the sorted rotated array nums are unique.

def search(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1

# usage
print(search([4,5,6,7,0,1,2], 0))  # Output: 4

# Time Complexity: O(log n)
# Space Complexity: O(1)
