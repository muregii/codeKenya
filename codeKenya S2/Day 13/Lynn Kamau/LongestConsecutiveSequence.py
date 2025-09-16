# Longest Consecutive Sequence Leetcode Challenge
# Given an array of integers nums, return the length of the longest consecutive sequence of elements that can be formed.
# A consecutive sequence is a sequence of elements in which each element is exactly 1 greater than the previous element. 
# The elements do not have to be consecutive in the original array.

def longest_consecutive(nums):
    num_set = set(nums)
    longest = 0
    for num in nums:
        if num - 1 not in num_set:
            length = 0
            while num + length in num_set:
                length += 1
            longest = max(longest, length)
    return longest

# Example Usage
print(longest_consecutive([2,20,4,10,3,4,5]))
print(longest_consecutive([0,3,2,5,4,6,1,1]))


# Time Complexity: O(n)
# Space Complexity: O(n)
