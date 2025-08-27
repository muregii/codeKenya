"""Given a sorted array of unique integers and a target integer,
 return true if there exists a pair of numbers that sum to target, false otherwise"""
from typing import List

def twoSumSorted( nums: List[int], target: int) -> bool:
    left = 0
    right = len(nums)-1

    while left < right:
        if nums[left] + nums[right] == target:
            return True
        elif nums[left] + nums[right] < target: #[1,2,3,4,5] target = 8
            left +=1
        else:
            right -=1
    return False

test_arr = [1,2,3,4,5]
target = 90
res = twoSumSorted(test_arr, target)
print(res)
