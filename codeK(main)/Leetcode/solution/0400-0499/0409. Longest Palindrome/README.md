# Leetcode - Longest Palindrome

## Problem Description

Given a string `s` which consists of lowercase or uppercase letters, return the length of the **longest** **palindrome** that can be built with those letters.

Letters are **case sensitive**, for example, `"Aa"` is not considered a palindrome.

**Constraints:**
- `1 <= s.length <= 2000`
- `s` consists of lowercase and/or uppercase English letters only.

## Solution

To find the length of the longest palindrome that can be built with the letters in the string `s`, we need to count how many times each letter appears in `s`. 


Imagine you have a bunch of toy letters. A palindrome is like a mirror image—you could fold it in half and both sides would match exactly. We want to build the longest toy word where if you folded it, it would look the same on both sides. To do this, you need pairs of letters. For example, to have the word "racecar," you need pairs of "r," "a," and "c," and one "e" that can sit in the middle.


Here are the steps:

1. **Count Letter Frequencies:**
   - Use a dictionary or a counter to count how many times each letter appears in `s`.

2. **Calculate Pairs and Extras:**
   - For each letter, see how many pairs you can make (divide by 2 and take the floor value).
   - If there are any letters left over after making pairs, you can use one of them to sit in the middle of the palindrome.

3. **Build the Longest Palindrome:**
   - Add up the pairs of letters to get the base length of the palindrome.
   - If you have any leftover letters, you can add one to the base length to account for the middle character.

By counting how many times each letter appears, we can determine how many pairs we can make. Each pair contributes two characters to the palindrome. If there are any leftover letters after making pairs, one of them can be used as the middle character in the palindrome, which makes it possible to have an odd length.


```python
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
```

## Usage

To use the solution, create an instance of the `Solution` class and call the `longestPalindrome` method with the string `s`:

```python
solution = Solution()
s = "abccccdd"
result = solution.longestPalindrome(s)
print(result)  # Output: 7, because we can build the palindrome "dccaccd"
```

[Link to detailed explanation on GeeksforGeeks](https://www.geeksforgeeks.org/longest-palindromic-subsequence-dp-12/)


[Link to detailed explanation on Medium](https://medium.com/@ChrisBader/code-conquer-leetcode-5-longest-palindromic-substring-6ed45c257139)


[Link to detailed explanation on AlgoMonster](https://algo.monster/liteproblems/409)

## Check Out This Video

[![Video Explanation](https://img.youtube.com/vi/DSEng0xILV4/mqdefault.jpg)](https://youtu.be/DSEng0xILV4)


[![Video Explanation](https://img.youtube.com/vi/_g9jrLuAphs/mqdefault.jpg)](https://youtu.be/_g9jrLuAphs)


[![Video Explanation](https://img.youtube.com/vi/gjYSovOESAU/mqdefault.jpg)](https://youtu.be/gjYSovOESAU)


## Complexity Analysis

- **Time Complexity:** O(n), where `n` is the length of the string `s`. We iterate through the string once to count the characters and once to calculate the palindrome length.
- **Space Complexity:** O(1), as we are using a constant amount of extra space for the character counts and a few variables. The size of the alphabet is fixed, and thus the space needed to store the counts is also constant.