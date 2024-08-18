# Leetcode - Sort the Jumbled Numbers

## Problem Description

You are given a **0-indexed** integer array `mapping` which represents the mapping rule of a shuffled decimal system. `mapping[i] = j` means digit `i` should be mapped to digit `j` in this system.

The **mapped value** of an integer is the new integer obtained by replacing each occurrence of digit `i` in the integer with `mapping[i]` for all `0 <= i <= 9`.

You are also given another integer array `nums`. Return *the array `nums` sorted in **non-decreasing** order based on the **mapped values** of its elements*.

**Notes:**
- Elements with the same mapped values should appear in the **same relative** order as in the input.
- The elements of `nums` should only be sorted based on their mapped values and **not be replaced** by them.

**Constraints:**
- `mapping.length == 10`
- `0 <= mapping[i] <= 9`
- All the values of `mapping[i]` are **unique**.
- `1 <= nums.length <= 3 * 10^4`
- `0 <= nums[i] < 10^9`

## Solution

**Understanding the Problem:**
   - We are given two arrays: `mapping` and `nums`.
   - The `mapping` array provides a rule for transforming each digit from `0` to `9` into another digit.
   - Our task is to sort the numbers in `nums` based on the values they transform into using the mapping rules.

**Breaking It Down**
   - **Mapping the Digits.** 
     Each digit of a number in `nums` is replaced according to the `mapping` array to form a new "mapped value." 
     For example, if `mapping = [2, 1, 4, 8, 6, 3, 0, 9, 7, 5]`, the digit `0` becomes `2`, `1` becomes `1`, and so on.
     
   - **Sorting the Data.**
     To sort `nums` by their mapped values, we need to:
     1. Convert each number in `nums` to its mapped value using the `mapping` array.
     2. Sort the numbers in `nums` according to these mapped values.
     3. If two numbers have the same mapped value, maintain their relative order from the input.
     
   - **Implementation Approach.**
     We can create a helper function that converts a number to its mapped value by transforming each digit. We then use this helper function to sort `nums`.

**Algorithm Steps:**
   - Define a helper function `convert` that takes a number and returns its mapped value as per the `mapping` array.
   - Sort `nums` using Python's `sorted` function, where the key is the mapped value obtained using the `convert` function.
   - Return the sorted list.

### Python Code

```python
class Solution(object):
    def sortJumbled(self, mapping, nums):
        """
        :type mapping: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        
```

### Example

```python
# Input
mapping = [2,1,4,8,6,3,0,9,7,5]
nums = [990, 332, 981]

# Output
[981, 990, 332]
```

### Explanation
1. Map each digit of the numbers using `mapping`:
   - `990` becomes `775`
   - `332` becomes `884`
   - `981` becomes `715`
2. Sort the numbers based on their mapped values: `[715 (981), 775 (990), 884 (332)]`.
3. The sorted array based on these mapped values is: `[981, 990, 332]`.

### Usage

To use the solution, create an instance of the `Solution` class and call the `sortJumbled` method with the `mapping` and `nums` arrays:

```python
# Example usage
solution = Solution()
mapping = [2,1,4,8,6,3,0,9,7,5]
nums = [990, 332, 981]
sorted_nums = solution.sortJumbled(mapping, nums)
print(sorted_nums)  # Output: [981, 990, 332]
```

### Additional Resources

[Link to detailed explanation on Algo Monster](https://algo.monster/liteproblems/2191)

### Check Out These Video(s)

[![Video Explanation](https://img.youtube.com/vi/rmkF2mxPoZM/mqdefault.jpg)](https://youtu.be/rmkF2mxPoZM)


### Complexity Analysis

- **Time Complexity:** O(n log n), where `n` is the length of the `nums` array. The sorting step takes `O(n log n)`, and converting the numbers takes linear time.
- **Space Complexity:** O(n), for storing the mapped values and the sorted result array.