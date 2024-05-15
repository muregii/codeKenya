# Leetcode - Largest Positive Integer That Exists With Its Negative

## Problem Description

Given an integer array `nums` that **does not contain** any zeros, find the **largest positive integer k** such that `-k` also exists in the array.

Return *the positive integer k*. If there is no such integer, return -1.

## Solution

To solve this problem, we can use a set to efficiently check if the negative counterpart of each element exists in the array.

Here's how we can approach this problem:

1. Initialize an empty set `seen` to store the unique elements encountered in the array.
2. Iterate through each element `num` in the array `nums`.
3. If `-num` exists in the `seen` set, update the maximum positive integer `k` found so far.
4. Add the current element `num` to the `seen` set.
5. After iterating through all elements, return the maximum positive integer `k` found. If no such integer exists, return -1.

By using a set to efficiently check for existence, we can find the largest positive integer `k` satisfying the given condition.

## Usage

To use the solution, create an instance of the `Solution` class and call the `findMaxK` method with the input parameter `nums`:

```python
solution = Solution()
# Define the input array nums
# nums = [3, 2, -1, -4, 5, 6]
# Call the findMaxK method
result = solution.findMaxK(nums)
print(result)
```

```python
# nums = [3, 2, -1, -4, 5, 6]
```

[Link to detailed explanation on Geeksforgeeks](https://www.geeksforgeeks.org/largest-number-having-both-positive-and-negative-values-present-in-the-array/?ref=gcse)



[Link to detailed explanation on Geeksforgeeks](https://www.geeksforgeeks.org/representation-of-negative-binary-numbers/)

## Check Out this video

[![Video Explanation](https://img.youtube.com/vi/LZaWj13_D6o/mqdefault.jpg)](https://youtu.be/LZaWj13_D6o)


## Complexity Analysis

- **Time Complexity:** O(n), where n is the length of the input array `nums`. We iterate through each element once.
- **Space Complexity:** O(n), where n is the length of the input array `nums`. We use additional space for the set `seen` to store unique elements.