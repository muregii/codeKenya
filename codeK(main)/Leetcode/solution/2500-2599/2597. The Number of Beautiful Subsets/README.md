# Leetcode - The Number of Beautiful Subsets

## Problem Description

You are given an array `nums` of positive integers and a **positive** integer `k`.

A subset of `nums` is **beautiful** if it does not contain two integers with an absolute difference equal to `k`.

Return *the number of **non-empty beautiful** subsets of the array `nums`*.

A subset of `nums` is an array that can be obtained by deleting some (possibly none) elements from `nums`. Two subsets are different if and only if the chosen indices to delete are different.

**Constraints:**
- `1 <= nums.length <= 20`
- `1 <= nums[i], k <= 1000`

## Solution

Generate all possible subsets of the given array `nums` and then check if each subset is beautiful.

Think of a set of toys. We want to find all possible groups of toys we can make. But there is a rule: we can't have two toys in the same group if their difference in age is exactly `k` years. We need to find all such groups and count how many there are."


The `beautifulSubsets` method takes an array `nums` and an integer `k` and returns the number of non-empty beautiful subsets of `nums`.

1. **Generating Subsets:**
   - Use a recursive approach with a helper function `dfs` to generate all subsets.
   - For each subset, check if it is beautiful by verifying that no two integers in the subset have an absolute difference equal to `k`.

2. **Algorithm:**
   - Use the `dfs` function to explore all possible subsets.
   - Start with an empty subset and iterate through the array, adding each element to the current subset and exploring further combinations recursively.
   - Check if the current subset is beautiful and count it if it is.

We start with an empty set and look at each toy (number). For each toy, we can either include it in our group or leave it out. After making a group, we check if the group follows the rule that no two toys have an age difference of exactly `k` years. If the group follows the rule, we count it. We do this for all possible groups.


```python

class Solution(object):
    def beautifulSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

```

## Usage

To use the solution, create an instance of the `Solution` class and call the `beautifulSubsets` method with the array `nums` and the integer `k`:

```python
solution = Solution()
nums = [1, 2, 3, 4]
k = 1
result = solution.beautifulSubsets(nums, k)
print(result)  # Output: 8
```

[Link to detailed explanation on AlgoMonster](https://algo.monster/liteproblems/2597)

[Link to detailed explanation on Geeksforgeeks](https://www.geeksforgeeks.org/number-subsets-product-less-k/)

[Link to detailed explanation on Geeksforgeeks](https://www.geeksforgeeks.org/backtracking-to-find-all-subsets/)


## Check Out this videos

[![Video Explanation](https://img.youtube.com/vi/Dle_SpjHTio/mqdefault.jpg)](https://youtu.be/Dle_SpjHTio)

[![Video Explanation](https://img.youtube.com/vi/xNRavrSTUHY/mqdefault.jpg)](https://youtu.be/xNRavrSTUHY)

[![Video Explanation](https://img.youtube.com/vi/014NzNPJNbY/mqdefault.jpg)](https://youtu.be/014NzNPJNbY)


## Complexity Analysis

- **Time Complexity:** O(2^n * n^2), where n is the length of the array `nums`. This is because we are generating all possible subsets and checking each subset for the beautiful condition, which takes O(n^2) time.
- **Space Complexity:** O(n * 2^n), where n is the length of the array `nums`. This is the space used to store all the subsets.
