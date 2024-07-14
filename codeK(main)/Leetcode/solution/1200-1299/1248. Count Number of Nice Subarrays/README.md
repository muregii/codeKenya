# Leetcode - Count Number of Nice Subarrays

## Problem Description

Given an array of integers `nums` and an integer `k`, a continuous subarray is called **nice** if there are exactly `k` odd numbers in it.

Return *the number of **nice** subarrays*.

**Constraints:**
- `1 <= nums.length <= 50000`
- `1 <= nums[i] <= 10^5`
- `1 <= k <= nums.length`

## Solution

To find the number of nice subarrays, count subarrays with exactly `k` odd numbers. This can be efficiently solved using a sliding window technique.

1. **Understanding the Problem:**
   - Find subarrays with exactly `k` odd numbers.
   - Use a sliding window approach to maintain a count of odd numbers in the current window.

2. **Using a Sliding Window Approach:**
   - Use two pointers to maintain a window with at most `k` odd numbers.
   - Count the number of subarrays ending at each position with exactly `k` odd numbers.

3. **Algorithm Steps:**
   - Initialize pointers and counters.
   - Expand the right pointer to include more elements.
   - When there are more than `k` odd numbers, move the left pointer to reduce the number of odd numbers.
   - Keep track of subarrays with exactly `k` odd numbers using a count of previous valid windows.

### Example

Suppose you have `nums = [1, 1, 2, 1, 1]` and `k = 3`.

1. Initialize pointers and counters.
2. Expand the right pointer to include more elements:
   - Window: `[1, 1, 2, 1, 1]`
   - Count of odd numbers: `3`
3. Since there are exactly `k` odd numbers, count the valid subarrays ending at each position.

### Python Code


```python
class Solution(object):
    def numberOfSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
```

### Usage

To use the solution, create an instance of the `Solution` class and call the `numberOfSubarrays` method with `nums` and `k`:

```python
solution = Solution()
nums = [1, 1, 2, 1, 1]
k = 3
result = solution.numberOfSubarrays(nums, k)
print(result)  # Output: 2
```

### Additional Resources

[Link to detailed explanation on GeeksforGeeks](https://www.geeksforgeeks.org/number-subarrays-m-odd-numbers/)

[Link to detailed explanation on Medium](https://medium.com/@theorangecloud.in/1248-count-number-of-nice-subarrays-leetcode-5c8eb1b13672)

[Link to detailed explanation on Algo Monster](https://algo.monster/liteproblems/1248)

### Check Out These Videos

[![Video Explanation](https://img.youtube.com/vi/4zNK0rhFfcA/mqdefault.jpg)](https://youtu.be/4zNK0rhFfcA)

[![Video Explanation](https://img.youtube.com/vi/atUJS7ArOY0/mqdefault.jpg)](https://youtu.be/atUJS7ArOY0)

[![Video Explanation](https://img.youtube.com/vi/dhu5_v2iY8E/mqdefault.jpg)](https://youtu.be/dhu5_v2iY8E)

### Complexity Analysis

- **Time Complexity:** O(n), where `n` is the length of `nums`. The complexity is dominated by the sliding window operation.
- **Space Complexity:** O(n), for storing the prefix counts.