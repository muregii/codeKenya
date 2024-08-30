# Leetcode - Make Two Arrays Equal by Reversing Subarrays

## Problem Description

You are given two integer arrays of equal length `target` and `arr`. In one step, you can select any **non-empty subarray** of `arr` and reverse it. You are allowed to make any number of steps.

Return *`true` if you can make `arr` equal to `target` or `false` otherwise*.

**Constraints:**
- `target.length == arr.length`
- `1 <= target.length <= 1000`
- `1 <= target[i] <= 1000`
- `1 <= arr[i] <= 1000`

## Solution

**Understanding the Problem:**
   - We have two integer arrays, `target` and `arr`, both of the same length.
   - We can reverse any subarray of `arr` any number of times.
   - The task is to determine if we can transform `arr` into `target` by applying these reversals.

**Breaking It Down**
   - **Key Observation:**
     - Reversing a subarray rearranges its elements but does not change the multiset of elements in the array. Thus, `arr` can only be transformed into `target` if both arrays have the exact same elements with the same frequencies.
     
   - **Using Sorting:**
     - Since reversing does not change the content of the array but only the order, sorting both `target` and `arr` will make it easy to compare them directly. If the sorted versions of both arrays are identical, then `arr` can be transformed into `target` by reversing appropriate subarrays.

**Implementation Approach:**
   - Sort both `target` and `arr` arrays.
   - Compare the sorted arrays. If they are equal, return `true`; otherwise, return `false`.

**Algorithm Steps:**
   - **Sort the Arrays:** Sort both `target` and `arr`.
   - **Compare the Sorted Arrays:** Check if the sorted versions of `target` and `arr` are identical.
   - **Return the Result:** If the sorted arrays match, return `true`; otherwise, return `false`.

### Python Code

```python
class Solution(object):
    def canBeEqual(self, target, arr):
        """
        :type target: List[int]
        :type arr: List[int]
        :rtype: bool
        """
```

### Example

```python
# Input
target = [1, 2, 3, 4]
arr = [2, 4, 1, 3]

# Output
True
```

### Explanation
1. **Sorting:** 
   - `target` sorted is `[1, 2, 3, 4]`.
   - `arr` sorted is also `[1, 2, 3, 4]`.
2. **Comparison:** Since the sorted arrays are identical, it is possible to rearrange `arr` to match `target` through a series of reversals.

### Usage

To use the solution, create an instance of the `Solution` class and call the `canBeEqual` method with the `target` and `arr` arrays:

```python
# Example usage
solution = Solution()
target = [1, 2, 3, 4]
arr = [2, 4, 1, 3]
result = solution.canBeEqual(target, arr)
print(result)  # Output: True
```

### Additional Resources

[Link to detailed explanation on Algo Monster](https://algo.monster/liteproblems/1460)

[Link to detailed explanation on Geeksforgeeks](https://www.geeksforgeeks.org/check-if-two-arrays-can-be-made-equal-by-reversing-any-subarray-once/)

[Link to detailed explanation on Geeksforgeeks](https://www.geeksforgeeks.org/check-if-two-arrays-can-be-made-equal-by-reversing-subarrays-multiple-times/)

[Link to detailed explanation on Geeksforgeeks](https://www.geeksforgeeks.org/check-if-two-arrays-are-equal-or-not/)

### Check Out These Video(s)

[![Video Explanation](https://img.youtube.com/vi/7YoDfM4RbZs/mqdefault.jpg)](https://youtu.be/7YoDfM4RbZs)

[![Video Explanation](https://img.youtube.com/vi/XJkd8HKGcQw/mqdefault.jpg)](https://youtu.be/XJkd8HKGcQw)

### Complexity Analysis

- **Time Complexity:** O(n log n), where `n` is the length of the arrays. The dominant factor is the sorting step.
- **Space Complexity:** O(n), where `n` is the length of the arrays. Space is needed to store the sorted versions of the arrays.