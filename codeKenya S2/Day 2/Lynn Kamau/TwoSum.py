#Two Sum Leetcode Problem Challenge
#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#You may assume that each input would have exactly one solution, and you may not use the same element twice.
#You can return the answer in any order.

def twoSum(nums, target):
    seen = {} 
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i


#TEST CASES
print(twoSum([2, 7, 11, 15], 9))        
print(twoSum([3, 2, 4], 6))             
print(twoSum([3, 3], 6))                
print(twoSum([1, 5, 1, 5], 10))         
print(twoSum([0, 4, 3, 0], 0))         
