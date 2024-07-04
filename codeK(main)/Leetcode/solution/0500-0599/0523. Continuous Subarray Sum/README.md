# Leetcode - Continuous Subarray Sum

## Problem Description

Given an integer array `nums` and an integer `k`, return *`true` if `nums` has a good subarray or `false` otherwise.*

A **good subarray** is a subarray where:
- Its length is **at least two**, and
- The sum of the elements of the subarray is a multiple of `k`.

**Note:**
- A **subarray** is a contiguous part of the array.
- An integer `x` is a multiple of `k` if there exists an integer `n` such that `x = n * k`. 
- `0` is always a multiple of `k`.

**Constraints:**
- `1 <= nums.length <= 10^5`
- `0 <= nums[i] <= 10^9`
- `0 <= sum(nums[i]) <= 2^31 - 1`
- `1 <= k <= 2^31 - 1`

## Solution

To determine if an array `nums` has a subarray with a sum that is a multiple of `k`, use the concept of **prefix sums** and **modulo operations**. This approach helps in efficiently checking for good subarrays without having to iterate over all possible subarrays explicitly.


Imagine you have a list of numbers and a special number `k`. You want to find if there is a piece of this list where the sum of the numbers is a multiple of `k`. For example, if you have numbers `[23, 2, 4, 6, 7]` and `k` is `6`, you want to find a piece like `[2, 4]` whose sum is `6` and `6` is a multiple of `6`.

The tricky part is finding the subarrays quickly. Checking every possible piece of the list can take too long, especially if the list is very large. So, we need a faster way to find if there is a subarray with a sum that’s a multiple of `k`.

Here are the steps:

1. **Calculate Prefix Sums and Remainders:**
   - A **prefix sum** is the sum of elements from the start of the list to a certain point.
   - Calculate the remainder when each prefix sum is divided by `k`.

2. **Use a Dictionary to Track Remainders:**
   - Use a dictionary to store the remainder and the index where it occurred.
   - If the same remainder occurs again later, it means the subarray between these two indices has a sum that is a multiple of `k`.

3. **Check for Good Subarrays:**
   - For each prefix sum, calculate its remainder.
   - If this remainder was seen before and the subarray length is at least `2`, we have found a good subarray.

By using prefix sums and keeping track of remainders in a dictionary, we can efficiently find subarrays whose sums are multiples of `k`. This approach ensures we don’t have to check every possible subarray explicitly.

```python
class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        
```

## Usage

To use the solution, create an instance of the `Solution` class and call the `checkSubarraySum` method with the array of numbers (`nums`) and the integer `k`:

```python
solution = Solution()
nums = [23, 2, 4, 6, 7]
k = 6
result = solution.checkSubarraySum(nums, k)
print(result)  # Output: True, because the subarray [2, 4] has a sum of 6 which is a multiple of 6.

nums = [23, 2, 6, 4, 7]
k = 13
result = solution.checkSubarraySum(nums, k)
print(result)  # Output: False, because there is no subarray whose sum is a multiple of 13.
```

[Link to detailed explanation on GeeksforGeeks](https://www.geeksforgeeks.org/largest-sum-contiguous-subarray/)

[Link to detailed explanation on Medium](https://medium.com/@sheefanaaz6417/523-continuous-subarray-sum-80598067d121)

[Link to detailed explanation on AlgoMonster](https://algo.monster/liteproblems/523)

## Check Out This Video

[![Video Explanation](https://img.youtube.com/vi/OKcrLfR-8mE/mqdefault.jpg)](https://youtu.be/OKcrLfR-8mE)

[![Video Explanation](https://img.youtube.com/vi/1W_HYBqvDLw/mqdefault.jpg)](https://youtu.be/1W_HYBqvDLw)

[![Video Explanation](https://img.youtube.com/vi/wmn3c1mP0pY/mqdefault.jpg)](https://youtu.be/wmn3c1mP0pY)

## Complexity Analysis

- **Time Complexity:** O(n), where `n` is the number of elements in `nums`. We iterate through the list once to compute prefix sums and check remainders.
- **Space Complexity:** O(min(n, k)), where `k` is the number of possible remainders. In the worst case, we store `n` remainders in the dictionary.