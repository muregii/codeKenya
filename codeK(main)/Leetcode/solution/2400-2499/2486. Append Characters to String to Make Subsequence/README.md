# Leetcode - Append Characters to String to Make Subsequence

## Problem Description

You are given two strings `s` and `t` consisting of only lowercase English letters.

*Return the minimum number of characters that need to be appended to the end of `s` so that `t` becomes a subsequence of `s`.*

A **subsequence** is a string that can be derived from another string by deleting some or no characters without changing the order of the remaining characters.

**Constraints:**
- `1 <= s.length, t.length <= 10^5`
- `s` and `t` consist only of lowercase English letters.

## Solution

To find the minimum number of characters that need to be appended to the end of `s` so that `t` becomes a subsequence of `s`, align the characters of `t` within `s`.


Imagine you have two strings, `s` and `t`. You want to make sure that by the time you finish `s`, you can see all the letters of `t` in the same order. If `t` is not fully there, you will need to add more letters to `s` to match `t`. Our goal is to find the least number of letters you need to add.


Let’s break down the steps:

1. **Use Two Pointers:**
   - One pointer will iterate through `s` (`s_index`), and another will iterate through `t` (`t_index`).
   - For each character in `s`, if it matches the current character in `t`, we move the `t_index` to the next character in `t`.
   - If we reach the end of `t` (i.e., `t_index` equals the length of `t`), then `t` is already a subsequence of `s`, and no characters need to be added.

2. **Calculate Additional Characters:**
   - If we finish iterating through `s` and haven’t finished `t`, the number of characters left in `t` is what we need to append to `s`.


We start by looking at each character in `s` and compare it to the characters in `t`. If we find a character in `s` that matches the current character in `t`, we move to the next character in `t`. Once we finish `s`, if we still have characters left in `t`, we need to add those characters to `s` to make `t` a subsequence.


```python
class Solution(object):
    def appendCharacters(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
```

## Usage

To use the solution, create an instance of the `Solution` class and call the `appendCharacters` method with the strings `s` and `t`:

```python
solution = Solution()
s = "abcde"
t = "ace"
result = solution.appendCharacters(s, t)
print(result)  # Output: 0, because "ace" is already a subsequence of "abcde"

s = "abc"
t = "abcd"
result = solution.appendCharacters(s, t)
print(result)  # Output: 1, because we need to add "d" to the end of "abc" to get "abcd"
```

[Link to detailed explanation on Algo Monster](https://algo.monster/liteproblems/2486)


[Link to detailed explanation on Geeksforgeeks](https://www.geeksforgeeks.org/minimum-subsequences-of-a-string-a-required-to-be-appended-to-obtain-the-string-b/)


[Link to detailed explanation on Medium](https://medium.com/@jjyk/leetcode-2486-append-characters-to-string-to-make-subsequence-68ad4be83ad9)





## Check Out this video

[![Video Explanation](https://img.youtube.com/vi/gKDmO8ZLRD8/mqdefault.jpg)](https://youtu.be/gKDmO8ZLRD8)


[![Video Explanation](https://img.youtube.com/vi/s8ZaYDuYqmo/mqdefault.jpg)](https://youtu.be/s8ZaYDuYqmo)


[![Video Explanation](https://img.youtube.com/vi/WVDQWJuzLmw/mqdefault.jpg)](https://youtu.be/WVDQWJuzLmw)



## Complexity Analysis

- **Time Complexity:** O(n + m), where `n` is the length of `s` and `m` is the length of `t`. We iterate through both strings once.
- **Space Complexity:** O(1), as we are using a constant amount of extra space to keep track of the indices.