# Find the minimum element in a rotated sorted array Leetcode Problem
# You are given an array of length n which was originally sorted in ascending order. 
# It has now been rotated between 1 and n times. For example, the array nums = [1,2,3,4,5,6] might become:[3,4,5,6,1,2] if it was rotated 4 times.[1,2,3,4,5,6] if it was rotated 6 times.
# Notice that rotating the array 4 times moves the last four elements of the array to the beginning. Rotating the array 6 times produces the original array.
# Assuming all elements in the rotated sorted array nums are unique, return the minimum element of this array.


def find_min(nums):
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid
    return nums[left]

# usage
print(find_min([3,4,5,6,1,2]))
print(find_min([4,5,0,1,2,3]))
print(find_min([4,5,6,7]))

# Time Complexity: O(log n)
# Space Complexity: O(1)