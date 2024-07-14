# Leetcode - Longest Subarray with Limit

## Problem Description

Given an array of integers `nums` and an integer `limit`, return the size of the longest **non-empty** subarray such that the absolute difference between any two elements of this subarray is less than or equal to `limit`.

**Constraints:**
- `1 <= nums.length <= 10^5`
- `1 <= nums[i] <= 10^9`
- `0 <= limit <= 10^9`

## Solution

To find the size of the longest subarray where the absolute difference between any two elements is less than or equal to `limit`, use a sliding window approach with two deques to keep track of the minimum and maximum values in the current window.

1. **Understanding the Problem:**
   - Find the longest subarray where the difference between the maximum and minimum values is at most `limit`.
   - Use a sliding window to maintain the current subarray and dynamically adjust its size to meet the condition.

2. **Using a Sliding Window Approach:**
   - Use two deques to keep track of the indices of the minimum and maximum values in the current window.
   - Expand the window by moving the right pointer.
   - If the condition is violated (i.e., the difference between the maximum and minimum values exceeds `limit`), shrink the window by moving the left pointer.

3. **Algorithm Steps:**
   - Initialize pointers and deques.
   - Expand the right pointer to include more elements while maintaining the deques.
   - If the condition is violated, move the left pointer to restore the condition.
   - Keep track of the maximum window size that meets the condition.

### Example

Suppose you have `nums = [8, 2, 4, 7]` and `limit = 4`.

1. Initialize pointers and deques.
2. Expand the right pointer to include more elements:
   - Window: `[8, 2]`
   - Max value: `8`, Min value: `2`
   - Difference: `6` (exceeds limit), move left pointer to reduce window size.
3. Adjust window and continue:
   - Window: `[2, 4, 7]`
   - Max value: `7`, Min value: `2`
   - Difference: `5` (exceeds limit), move left pointer to reduce window size.
4. Resulting maximum window size that meets the condition is `2`.

### Python Code


```python
class Solution(object):
    def longestSubarray(self, nums, limit):
        """
        :type nums: List[int]
        :type limit: int
        :rtype: int
        """
        from collections import deque
        
        
```

### Usage

To use the solution, create an instance of the `Solution` class and call the `longestSubarray` method with `nums` and `limit`:

```python
solution = Solution()
nums = [8, 2, 4, 7]
limit = 4
result = solution.longestSubarray(nums, limit)
print(result)  # Output: 2
```

### Additional Resources

[Link to detailed explanation on Geeksforgeeks](https://www.geeksforgeeks.org/longest-subarray-in-which-absolute-difference-between-any-two-element-is-not-greater-than-x/)

[Link to detailed explanation on Algo Monster](https://algo.monster/liteproblems/1438)

### Check Out These Videos

[![Video Explanation](https://img.youtube.com/vi/V-ecDfY5xEw/mqdefault.jpg)](https://youtu.be/V-ecDfY5xEw)

[![Video Explanation](https://img.youtube.com/vi/LDFZm4iB7tA/mqdefault.jpg)](https://youtu.be/LDFZm4iB7tA)

[![Video Explanation](https://img.youtube.com/vi/dlvajECagM4/mqdefault.jpg)](https://youtu.be/dlvajECagM4)

### Complexity Analysis

- **Time Complexity:** O(n), where `n` is the length of `nums`. The complexity is dominated by the sliding window operation and deque operations.
- **Space Complexity:** O(n), for storing the indices in the deques.