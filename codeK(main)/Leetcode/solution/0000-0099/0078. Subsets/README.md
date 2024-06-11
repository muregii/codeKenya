# Leetcode - Subsets (Power Set)

## Problem Description

Given an integer array `nums` of **unique** elements, *return all possible **subsets** (the power set)*.

The solution set **must not** contain duplicate subsets. Return the solution in any **order**.

**Constraints:**
- `1 <= nums.length <= 10`
- `-10 <= nums[i] <= 10`
- All the numbers of `nums` are **unique**.

## Solution

Generate all possible subsets (or combinations) of the given array `nums`.


Think of a set of different toys. You want to find all possible groups of toys you can make, including not picking any toys at all. We want to list all these groups. For example, if you have three toys: a ball, a car, and a doll, the possible groups (subsets) you can make are: 
1. No toys at all
2. Just the ball
3. Just the car
4. Just the doll
5. The ball and the car
6. The ball and the doll
7. The car and the doll
8. All three toys: the ball, the car, and the doll.


The `subsets` method takes an array `nums` and returns all possible subsets of `nums`.

1. **Generating Subsets:**
   - We can generate all possible subsets of the array using a recursive approach. Each element can either be included in a subset or not.
   - For each element, we recursively generate subsets that include the element and subsets that do not.

2. **Algorithm:**
   - Use a helper function to recursively generate subsets.
   - Start with an empty subset and iterate through the array, adding each element to the subset and exploring further combinations recursively.


We start with an empty set and look at each toy (number). For each toy, we can either include it in our group or leave it out. We do this for all toys and list all the possible groups.

```python

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
```

## Usage

To use the solution, create an instance of the `Solution` class and call the `subsets` method with the array `nums`:

```python
solution = Solution()
nums = [1, 2, 3]
result = solution.subsets(nums)
print(result)  # Output: [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]
```


[Link to detailed explanation on AlgoMonster](https://algo.monster/liteproblems/78)

[Link to detailed explanation on Medium](https://medium.com/@qklu/leetcode-78-subsets-5a79d7c271cb)

[Link to detailed explanation on Geeksforgeeks](https://www.geeksforgeeks.org/backtracking-to-find-all-subsets/?ref=gcse)


## Check Out this videos

[![Video Explanation](https://img.youtube.com/vi/REOH22Xwdkk/mqdefault.jpg)](https://youtu.be/REOH22Xwdkk)

[![Video Explanation](https://img.youtube.com/vi/UP3dOYJa05s/mqdefault.jpg)](https://youtu.be/UP3dOYJa05s)

[![Video Explanation](https://img.youtube.com/vi/3tpjp5h3M6Y/mqdefault.jpg)](https://youtu.be/3tpjp5h3M6Y)

[![Video Explanation](https://img.youtube.com/vi/h4zNvA4lbtc/mqdefault.jpg)](https://youtu.be/h4zNvA4lbtc)



## Complexity Analysis

- **Time Complexity:** O(2^n), where n is the length of the array `nums`. This is because we are generating all possible subsets.
- **Space Complexity:** O(n * 2^n), where n is the length of the array `nums`. This is the space used to store all the subsets.