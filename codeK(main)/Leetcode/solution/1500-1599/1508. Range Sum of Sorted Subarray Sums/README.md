# Leetcode - Range Sum of Sorted Subarray Sums

## Problem Description

You are given the array `nums` consisting of `n` positive integers. You compute the sum of all non-empty continuous subarrays from the array and then sort them in non-decreasing order, creating a new array of `n * (n + 1) / 2` numbers.

Return *the sum of the numbers from index `left` to index `right` (indexed from 1), inclusive, in the new array*. Since the answer can be a huge number, return it modulo `10^9 + 7`.

**Constraints:**
- `n == nums.length`
- `1 <= nums.length <= 1000`
- `1 <= nums[i] <= 100`
- `1 <= left <= right <= n * (n + 1) / 2`

## Solution

**Understanding the Problem:**
   - We need to compute the sum of all possible non-empty subarrays of the given `nums` array.
   - These subarrays' sums will be stored in a new array, which is then sorted in non-decreasing order.
   - The task is to return the sum of the elements from index `left` to index `right` in this sorted array.

**Breaking It Down**
   - **Generate Subarray Sums:**
     - For every possible subarray in `nums`, calculate its sum and store these sums in an array.
     - Given `n` elements in `nums`, there are `n * (n + 1) / 2` subarrays.
     
   - **Sort and Sum Subarrays:**
     - Sort the array of subarray sums.
     - Calculate the sum of the elements from the `left` to the `right` index in this sorted array.
     - Since the result might be large, take the sum modulo `10^9 + 7`.

**Implementation Approach:**
   - Iterate through the array `nums` to generate all possible subarray sums.
   - Sort the resulting subarray sums.
   - Calculate the sum of elements from index `left` to `right` in the sorted array, ensuring to apply modulo `10^9 + 7`.

**Algorithm Steps:**
   - **Generate Subarray Sums:** Iterate over all starting and ending positions in the array to calculate sums of subarrays.
   - **Sort the Sums:** Sort the array of subarray sums.
   - **Calculate the Range Sum:** Sum the elements from `left` to `right` in the sorted array and apply the modulo operation.

### Python Code

```python
class Solution(object):
    def rangeSum(self, nums, n, left, right):
        """
        :type nums: List[int]
        :type n: int
        :type left: int
        :type right: int
        :rtype: int
        """
        
```

### Example

```python
# Input
nums = [1, 2, 3, 4]
n = 4
left = 3
right = 6

# Output
13
```

### Explanation
1. **Subarray Sums:** The subarrays and their sums are as follows:
   - `[1] = 1`
   - `[1, 2] = 3`
   - `[1, 2, 3] = 6`
   - `[1, 2, 3, 4] = 10`
   - `[2] = 2`
   - `[2, 3] = 5`
   - `[2, 3, 4] = 9`
   - `[3] = 3`
   - `[3, 4] = 7`
   - `[4] = 4`
2. **Sorted Subarray Sums:** After sorting, the subarray sums are `[1, 2, 3, 3, 4, 5, 6, 7, 9, 10]`.
3. **Range Sum:** The sum from index `left` to `right` is `3 + 3 + 4 + 5 = 13`.

### Usage

To use the solution, create an instance of the `Solution` class and call the `rangeSum` method with the `nums`, `n`, `left`, and `right` parameters:

```python
# Example usage
solution = Solution()
nums = [1, 2, 3, 4]
n = 4
left = 3
right = 6
result = solution.rangeSum(nums, n, left, right)
print(result)  # Output: 13
```

### Additional Resources

[Link to detailed explanation on Algo Monster](https://algo.monster/liteproblems/1508)

[Link to detailed explanation on Geeksforgeeks](https://www.geeksforgeeks.org/number-of-subarrays-having-sum-in-a-given-range/)

### Complexity Analysis

- **Time Complexity:** O(n^2 log n), where `n` is the length of the array. Generating subarray sums is O(n^2), and sorting them takes O(n^2 log n).
- **Space Complexity:** O(n^2), for storing the subarray sums.