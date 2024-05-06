# Leetcode - Longest Ideal String

## Problem Description

You are given a string `s` consisting of lowercase letters and an integer `k`. We call a string `t` ideal if the following conditions are satisfied:

1. `t` is a subsequence of the string `s`.
2. The absolute difference in the alphabet order of every two adjacent letters in `t` is less than or equal to `k`.

Return the length of the `longest` ideal string.

A `subsequence` is a string that can be derived from another string by deleting some or no characters without changing the order of the remaining characters.

Note that the alphabet order is not cyclic. For example, the absolute difference in the alphabet order of 'a' and 'z' is 25, not 1.

## Solution

To solve this problem, we can use dynamic programming. We'll define a function `dp` to represent the length of the longest ideal string ending at position `i` in the input string `s`.

Here's how we can approach this problem:

1. Initialize an array `dp` of size `n`, where `n` is the length of the input string `s`.
2. Initialize each element of `dp` to 1, as each individual character itself forms a valid ideal string.
3. Iterate through each character `s[i]` in the input string `s`.
4. For each character `s[i]`, iterate through all characters `s[j]` before it (where `j < i`) to find the character with the maximum absolute difference in alphabet order that is less than or equal to `k`.
5. Update `dp[i]` with the maximum value of `dp[j] + 1` found in step 4.
6. Return the maximum value in the `dp` array as the length of the longest ideal string.

By dynamically calculating the length of the longest ideal string ending at each position in the input string `s`, we can determine the overall maximum length of an ideal string.

## Usage

To use the solution, create an instance of the `Solution` class and call the `longestIdealString` method with the input parameters `s` and `k`:

```python
solution = Solution()
# Define the input string and integer k
# s = "abcde"
# k = 2
# Call the longestIdealString method
result = solution.longestIdealString(s, k)
print(result)
```

```python
# s = "abcde"
# k = 2
```

## Check Out this video


[![Video Explanation](https://img.youtube.com/vi/gR1E2oLQYSY/mqdefault.jpg)](https://youtu.be/gR1E2oLQYSY)



## Complexity Analysis

- **Time Complexity:** O(n^2), where n is the length of the input string `s`. We have nested loops to iterate through all possible pairs of characters in the string.
- **Space Complexity:** O(n), where n is the length of the input string `s`. We use additional space to store the dynamic programming array `dp`.