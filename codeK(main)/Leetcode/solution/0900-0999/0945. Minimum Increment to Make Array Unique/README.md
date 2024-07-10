# Leetcode - Minimum Increment to Make Array Unique

## Problem Description

You are given an integer array `nums`. In one move, you can pick an index `i` where `0 <= i < nums.length` and increment `nums[i]` by 1.

Return *the minimum number of moves to make every value in `nums` **unique**.*

The test cases are generated so that the answer fits in a 32-bit integer.

**Constraints:**
- `1 <= nums.length <= 10^5`
- `0 <= nums[i] <= 10^5`

## Solution

To find the minimum number of moves required to make all elements in the `nums` array unique:

1. **Understanding the Problem:**
   - We have an array `nums` with potentially duplicate values.
   - The task is to make all elements in the array unique by incrementing any element by 1 in each move.
   - The challenge is to minimize the total number of such moves.

2. **Sorting for Efficient Processing:**
   - By sorting the `nums` array, we can easily compare each element with the previous one to ensure uniqueness.
   - If an element is not unique, we can increment it to the next possible unique value.

3. **Increment to Ensure Uniqueness:**
   - Iterate through the sorted array and for each element, if it is not greater than the previous element, increment it to be one more than the previous element.
   - Keep track of the total number of increments (moves) needed.

### Example

Suppose you have `nums = [3, 2, 1, 2, 1, 7]`.

1. Sort `nums`:
   - Sorted `nums = [1, 1, 2, 2, 3, 7]`
   
2. Process each element:
   - The first element is `1` (no increment needed).
   - The second element is also `1`, increment to `2` (1 move).
   - The third element is `2`, increment to `3` (1 move).
   - The fourth element is `2`, increment to `4` (2 moves).
   - The fifth element is `3`, increment to `5` (2 moves).
   - The sixth element is `7` (no increment needed).
   
3. Total minimum moves: `1 + 1 + 2 + 2 = 6`.

### Python Code



```python
class Solution(object):
    def minIncrementForUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
```

### Usage

To use the solution, create an instance of the `Solution` class and call the `minIncrementForUnique` method with `nums`:

```python
solution = Solution()
nums = [3, 2, 1, 2, 1, 7]
result = solution.minIncrementForUnique(nums)
print(result)  # Output: 6
```

### Additional Resources

[Link to detailed explanation on GeeksforGeeks](https://www.geeksforgeeks.org/minimum-increment-operations-to-make-array-unique/)

[Link to detailed explanation on Medium](https://medium.com/@glynnnnnnnnn/minimum-increment-to-make-array-unique-e311ef431ca8)

[Link to detailed explanation on AlgoMonster](https://algo.monster/liteproblems/945)

### Check Out These Videos

[![Video Explanation](https://img.youtube.com/vi/XPPs2Wj2YSk/mqdefault.jpg)](https://youtu.be/XPPs2Wj2YSk)

[![Video Explanation](https://img.youtube.com/vi/ZaAUHvocVcQ/mqdefault.jpg)](https://youtu.be/ZaAUHvocVcQ)

[![Video Explanation](https://img.youtube.com/vi/Nt-WwVzzJqo/mqdefault.jpg)](https://youtu.be/Nt-WwVzzJqo)

### Complexity Analysis

- **Time Complexity:** O(n log n), where `n` is the length of the `nums` array. The complexity is dominated by the sorting step.
- **Space Complexity:** O(1), since no additional space proportional to the input size is required. The calculations are performed in-place.