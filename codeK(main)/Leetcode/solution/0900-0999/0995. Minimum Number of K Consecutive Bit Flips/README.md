# Leetcode - Minimum Number of K Consecutive Bit Flips

## Problem Description

You are given a binary array `nums` and an integer `k`.

A **k-bit flip** is choosing a **subarray** of length `k` from `nums` and simultaneously changing every `0` in the subarray to `1`, and every `1` in the subarray to `0`.

*Return the minimum number of `k-bit flips` required so that there is no `0` in the array. If it is not possible, return `-1`.*

A **subarray** is a **contiguous** part of an array.

**Constraints:**
- `1 <= nums.length <= 10^5`
- `1 <= k <= nums.length`

## Solution

To find the minimum number of k-bit flips required so that there is no 0 in the array, use a sliding window technique with a queue to keep track of the flips.

1. **Understanding the Problem:**
   - We need to flip k consecutive bits in the array to change all 0s to 1s.
   - If a flip is performed at index `i`, it will affect the subarray starting at `i` and ending at `i+k-1`.

2. **Using a Sliding Window Approach:**
   - Use a queue to keep track of the end of the flips.
   - Expand the window by moving the right pointer.
   - If a 0 is found at the current position and it's not within a flip window, perform a flip and record the end of the flip.
   - If it’s not possible to flip, return -1.

3. **Algorithm Steps:**
   - Initialize pointers and a queue.
   - Iterate through the array and expand the window.
   - If a flip is needed, perform it and record the end position in the queue.
   - If a flip cannot be performed due to constraints, return -1.
   - Return the total number of flips performed.

### Example

Suppose you have `nums = [0, 1, 0]` and `k = 1`.

1. Initialize pointers and a queue.
2. Iterate through the array:
   - At index 0, a flip is needed. Flip the subarray `[0]` to `[1]` and record the end position in the queue.
   - At index 1, no flip is needed.
   - At index 2, a flip is needed. Flip the subarray `[0]` to `[1]` and record the end position in the queue.
3. The minimum number of flips required is `2`.

### Python Code

```python
class Solution(object):
    def minKBitFlips(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

```

### Usage

To use the solution, create an instance of the `Solution` class and call the `minKBitFlips` method with `nums` and `k`:

```python
solution = Solution()
nums = [0, 1, 0]
k = 1
result = solution.minKBitFlips(nums, k)
print(result)  # Output: 2
```

### Additional Resources

[Link to detailed explanation on Algo Monster Discuss](https://algo.monster/liteproblems/995)

[Link to detailed explanation on Geeksforgeeks Discuss](https://www.geeksforgeeks.org/minimum-bit-flips-such-that-every-k-consecutive-bits-contain-at-least-one-set-bit/)

[Link to detailed explanation on Medium Discuss](https://medium.com/algorithm-and-datastructure/minimum-number-of-k-consecutive-bit-flips-hard-problem-in-leetcode-995-cc86a73f816e)

### Check Out These Videos

[![Video Explanation](https://img.youtube.com/vi/Fv3M9uO5ovU/mqdefault.jpg)](https://youtu.be/Fv3M9uO5ovU)

[![Video Explanation](https://img.youtube.com/vi/oe9HR-cLAHo/mqdefault.jpg)](https://youtu.be/oe9HR-cLAHo)

### Complexity Analysis

- **Time Complexity:** O(n), where `n` is the length of `nums`. The complexity is dominated by the sliding window operation and queue operations.
- **Space Complexity:** O(k), for storing the indices in the queue.