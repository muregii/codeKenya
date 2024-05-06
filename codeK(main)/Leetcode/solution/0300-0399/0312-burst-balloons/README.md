# Leetcode - Burst Balloons

## Problem Description

You are given `n` balloons, indexed from 0 to `n - 1`. Each balloon is painted with a number on it represented by an array `nums`. You are asked to burst all the balloons.

If you burst the `ith` balloon, you will get `nums[i - 1] * nums[i] * nums[i + 1]` coins. If `i - 1` or `i + 1` goes out of bounds of the array, then treat it as if there is a balloon with a `1` painted on it.

Return the `maximum coins` you can collect by bursting the balloons wisely.

## Solution

To solve this problem, we can use dynamic programming. We can break down the problem into sub-problems where we burst balloons one by one and calculate the maximum coins for each subproblem.

Here's how we can approach this problem:

1. Define a function `dp` to represent the maximum coins that can be obtained by bursting balloons within the range `[left, right]`.
2. Iterate through the range `[left, right]` and choose a balloon `k` to burst last.
3. Calculate the coins obtained by bursting balloons within the range `[left, k - 1]`, `[k + 1, right]`, and the coins obtained by bursting the last balloon `k`.
4. Update the maximum coins for the current range `[left, right]` by considering all possible choices for the last balloon.
5. Repeat this process for all possible ranges `[left, right]`, starting from small ranges and gradually expanding.

By dynamically calculating the maximum coins for each subproblem, we can determine the overall maximum coins that can be obtained.

## Usage

To use the solution, create an instance of the `Solution` class and call the `maxCoins` method with the input parameter `nums`:

```python
solution = Solution()
# Define the array of balloons
# nums = [3,1,5,8]
# Call the maxCoins method
result = solution.maxCoins(nums)
print(result)
```

```python
# nums = [3,1,5,8]
```

[Link to detailed explanation on Medium](https://medium.com/algorithms-digest/bursting-balloons-1820664a4ffa)


## Check Out this video

[![Video Explanation](https://img.youtube.com/vi/VFskby7lUbw/mqdefault.jpg)](https://youtu.be/VFskby7lUbw)


[![Video Explanation](https://img.youtube.com/vi/KWPat-qNAGI/mqdefault.jpg)](https://youtu.be/KWPat-qNAGI)

## Complexity Analysis

- **Time Complexity:** O(n^3), where n is the number of balloons. We have nested loops to iterate through all possible ranges and choices for the last balloon.
- **Space Complexity:** O(n^2), where n is the number of balloons. We use a 2D array to store intermediate results for dynamic programming.