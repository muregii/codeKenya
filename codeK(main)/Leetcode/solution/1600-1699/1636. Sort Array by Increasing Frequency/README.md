# Leetcode - Sort the Array by Frequency

## Problem Description

Given an array of integers `nums`, sort the array in **increasing** order based on the frequency of the values. If multiple values have the same frequency, sort them in **decreasing** order.

Return *the sorted array*.

**Constraints:**
- `1 <= nums.length <= 100`
- `-100 <= nums[i] <= 100`

## Solution

**Understanding the Problem:**
   - We are given an array of integers, and we need to sort these integers based on how frequently they appear in the array.
   - If two integers have the same frequency, the larger number should come first in the sorted array.

**Breaking It Down**
   - **Organizing the Data.** 
     We have an array `nums`, and the first step is to determine how often each number appears in the array.
     
   - **Sorting the Data.**
     To sort the numbers by frequency and by value, we need to:
     1. Count the frequency of each number in the array.
     2. Sort the numbers first by their frequency (in increasing order) and then by their value (in decreasing order) when the frequency is the same.
     
   - **Implementation Approach.**
     We can use a dictionary to count the frequency of each number in the array. After that, we create a sorted list of the numbers based on the criteria mentioned. Finally, we reconstruct the array by repeating each number according to its frequency in the sorted order.

**Algorithm Steps:**
   - Use a dictionary to count the frequency of each number in `nums`.
   - Create a sorted list of the numbers, first by frequency (ascending) and then by value (descending).
   - Construct the result array by repeating each number according to its frequency in the sorted order.

### Python Code

```python
class Solution(object):
    def frequencySort(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
```

### Example

```python
# Input
nums = [1,1,2,2,2,3]

# Output
[3,1,1,2,2,2]
```

### Explanation
1. Count the frequency of each number: `{1: 2, 2: 3, 3: 1}`.
2. Sort the numbers by frequency and by value: `[3 (1 time), 1 (2 times), 2 (3 times)]`.
3. Construct the sorted array based on this order: `[3,1,1,2,2,2]`.

### Usage

To use the solution, create an instance of the `Solution` class and call the `frequencySort` method with the `nums` array:

```python
# Example usage
solution = Solution()
nums = [1,1,2,2,2,3]
sorted_nums = solution.frequencySort(nums)
print(sorted_nums)  # Output: [3,1,1,2,2,2]
```

### Additional Resources

[Link to detailed explanation on Algo Monster](https://algo.monster/liteproblems/1636)

[Link to detailed explanation on GeeksforGeeks](https://www.geeksforgeeks.org/sort-elements-by-frequency/)


### Check Out These Video(s)

[![Video Explanation](https://img.youtube.com/vi/Evq1SfUbhBg/mqdefault.jpg)](https://youtu.be/Evq1SfUbhBg)

[![Video Explanation](https://img.youtube.com/vi/VjnkNdsFikQ/mqdefault.jpg)](https://youtu.be/VjnkNdsFikQ)

[![Video Explanation](https://img.youtube.com/vi/S6UvwcpVnxc/mqdefault.jpg)](https://youtu.be/S6UvwcpVnxc)

### Complexity Analysis

- **Time Complexity:** O(n log n), where `n` is the length of the array. The sorting step takes `O(n log n)`, and counting the frequency of each element takes linear time.
- **Space Complexity:** O(n), for storing the frequency count and the sorted result array.