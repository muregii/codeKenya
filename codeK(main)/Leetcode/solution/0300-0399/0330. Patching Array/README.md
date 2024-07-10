# Leetcode - Patching Array

## Problem Description

Given a sorted integer array `nums` and an integer `n`, add/patch elements to the array such that any number in the range `[1, n]` inclusive can be formed by the sum of some elements in the array.

Return *the minimum number of patches required.*

**Constraints:**
- `1 <= nums.length <= 1000`
- `1 <= nums[i] <= 10^4`
- `nums is sorted in` **ascending order**.
- `1 <= n <= 2^31 - 1`

## Solution

To ensure any number in the range `[1, n]` can be formed by the sum of some elements in the array, we need to add the fewest possible numbers (patches) to cover all the gaps.

1. **Understanding the Problem:**
   - We need to ensure that every number from `1` to `n` can be represented as the sum of elements in `nums`.
   - The challenge is to determine the minimum number of additional elements (patches) required.

2. **Using a Greedy Approach:**
   - We will maintain a variable `miss`, which represents the smallest number that cannot be formed with the current array.
   - Iterate through the array and patch numbers if necessary to cover all gaps up to `n`.

3. **Algorithm Steps:**
   - Initialize `miss` to `1` and `added` (number of patches) to `0`.
   - Iterate through the array `nums` and check if `miss` can be formed.
   - If `miss` is less than the current number in `nums`, patch `miss` (i.e., add `miss` to the array).
   - Update `miss` by adding the patched value or the current array value.
   - Continue this process until `miss` exceeds `n`.

### Example

Suppose you have `nums = [1, 3]` and `n = 6`.

1. Initialize `miss = 1` and `added = 0`.
2. Iterate through `nums`:
   - `miss = 1`, `nums[0] = 1`: Since `miss` is covered, update `miss = 1 + 1 = 2`.
   - `miss = 2`, `nums[1] = 3`: `miss` is not covered, patch `miss` to cover it, update `miss = 2 + 2 = 4`, and `added = 1`.
   - `miss = 4`, `nums[1] = 3`: Since `miss` is covered, update `miss = 4 + 3 = 7`.
3. Final `miss = 7` which exceeds `n`, so the process stops with `added = 1`.

### Python Code


```python
class Solution(object):
    def minPatches(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: int
        """
        
```

### Usage

To use the solution, create an instance of the `Solution` class and call the `minPatches` method with `nums` and `n`:

```python
solution = Solution()
nums = [1, 3]
n = 6
result = solution.minPatches(nums, n)
print(result)  # Output: 1
```

### Additional Resources

[Link to detailed explanation on GeeksforGeeks](https://www.geeksforgeeks.org/monkey-patching-in-python-dynamic-behavior/?ref=gcse_ind)

[Link to detailed explanation on Medium](https://dreamume.medium.com/leetcode-330-patching-array-2477a76f40a0)

[Link to detailed explanation on AlgoMonster](https://algo.monster/liteproblems/330)

### Check Out These Videos

[![Video Explanation](https://img.youtube.com/vi/6s97yEBQaGQ/mqdefault.jpg)](https://youtu.be/6s97yEBQaGQ)

[![Video Explanation](https://img.youtube.com/vi/BfcU3NJuANg/mqdefault.jpg)](https://youtu.be/BfcU3NJuANg)

### Complexity Analysis

- **Time Complexity:** O(m + log n), where `m` is the length of the `nums` array. The complexity is dominated by the iteration through the array and patching process.
- **Space Complexity:** O(1), since no additional space proportional to the input size is required. The calculations are performed in-place.