"""Example 1: Given an array of positive integers nums and an integer k, find the length of the longest subarray whose sum is less than or equal to k. This is the problem we have been talking about above.

"""
from typing import List

@staticmethod
def longest_valid(nums: List[int], k: int) -> int:
    left = 0
    answer = 0
    curr = 0
    for right in range(len(nums)):
        curr += nums[right]
        while curr >= k:
            curr -= nums[left]
            left+=1
        answer = max(answer, right - left + 1)
        #print(f"{answer}")
    return answer
nums_test = [3, 1, 2, 7, 4, 2, 1, 1, 5]
k = 8.

res = longest_valid(nums_test, k)
print(res)