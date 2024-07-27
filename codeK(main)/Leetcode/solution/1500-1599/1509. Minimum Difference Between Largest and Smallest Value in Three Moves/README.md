# Leetcode - Minimum Difference Between Largest and Smallest Value in Three Moves

## Problem Description

You are given an integer array `nums`. 

In one move, you can choose one element of `nums` and change it to **any value**. 

Return *the minimum difference between the largest and smallest value of `nums` **after performing at most three moves***.

**Constraints:**
- `1 <= nums.length <= 10^5`
- `-10^9 <= nums[i] <= 10^9`

## Solution

To minimize the difference between the largest and smallest values in `nums` after at most three moves, leverage sorting and focus on the smallest possible ranges after removing up to three of the largest or smallest elements.

1. **Understanding the Problem:**
   - Minimize the difference between the largest and smallest elements after making at most three changes.
   - Changing an element means, reduce the highest values or increase the lowest values to minimize the range.

2. **Sorting the Array:**
   - Sorting the array helps us easily access the smallest and largest elements.
   - By considering the possible scenarios of removing up to three largest or smallest elements, we can evaluate the smallest difference.

3. **Algorithm Steps:**
   - Sort the array.
   - Consider the difference between the highest and lowest values after removing up to three elements from either end.
   - Calculate the minimum of these possible differences.

### Example

Suppose you have the following array:

```
nums = [5, 3, 2, 4, 1]
```

- Sort the array: `[1, 2, 3, 4, 5]`
- Evaluate possible scenarios:
  - Remove the three largest elements: difference between the 4th smallest and 1st smallest: `nums[2] - nums[0] = 3 - 1 = 2`
  - Remove the two largest and one smallest element: difference between the 3rd smallest and 2nd smallest: `nums[3] - nums[1] = 4 - 2 = 2`
  - Remove the one largest and two smallest elements: difference between the 2nd largest and 3rd smallest: `nums[4] - nums[2] = 5 - 3 = 2`
  - Remove the three smallest elements: difference between the 4th largest and 1st largest: `nums[3] - nums[0] = 4 - 1 = 3`

- The minimum difference after considering all scenarios is `2`.

### Python Code

```python
class Solution(object):
    def minDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
    
```

### Usage

To use the solution, create an instance of the `Solution` class and call the `minDifference` method with the array:

```python
solution = Solution()
nums = [5, 3, 2, 4, 1]
result = solution.minDifference(nums)
print(result)  # Output: 2
```

### Additional Resources

[Link to detailed explanation on Algo Monster](https://algo.monster/liteproblems/1509)

[Link to detailed explanation on Medium](https://medium.com/@okesseko/leetcode-day63-1509-3a7f400fcde8)

### Check Out These Videos

[![Video Explanation](https://img.youtube.com/vi/S3CJ0dcCXOY/mqdefault.jpg)](https://youtu.be/S3CJ0dcCXOY)

[![Video Explanation](https://img.youtube.com/vi/S6cUjbQuTnE/mqdefault.jpg)](https://youtu.be/S6cUjbQuTnE)

### Complexity Analysis

- **Time Complexity:** O(n log n), where `n` is the length of the array. This is due to the sorting operation.
- **Space Complexity:** O(1), as we only use a constant amount of extra space beyond the input array for storing the minimum differences.