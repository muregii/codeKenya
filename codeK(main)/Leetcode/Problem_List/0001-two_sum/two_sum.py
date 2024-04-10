#!/usr/bin/env python3

'''Given an array of integers nums and an integer target, 
return indices of the two numbers such that they add up to target.'''


class Solution(object):
    def twoSum(self, nums, target):

        complement_dict = {}

        for i, num in enumerate(nums):
            complement = target - num
            if complement in complement_dict:
                return [complement_dict[complement], i]
            complement_dict[num] = i
        return []
        