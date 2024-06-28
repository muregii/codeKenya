# Leetcode - Score of a String

## Problem Description

You are given a string `s`. The score of a string is defined as the sum of the absolute difference between the **ASCII** values of adjacent characters.

Return the **score** of `s`.

**Constraints:**
- `2 <= s.length <= 100`
- `s` consists only of lowercase English letters.

## Solution

Calculate the score of the string `s` by summing up the absolute differences between the ASCII values of adjacent characters.

Think of a string like a row of blocks with letters on them. Each letter has a number assigned to it based on the alphabet. Find out how different each pair of neighboring blocks is by subtracting their numbers and then adding up all these differences to get the total score.


The `scoreOfString` method takes a string `s` and returns the score of the string.

1. **Understanding ASCII Values:**
   - Each character has an ASCII value, which is a unique number assigned to it. For example, the ASCII value of 'a' is 97, 'b' is 98, and so on.

2. **Calculating Absolute Differences:**
   - To find the difference between two characters, we subtract their ASCII values.
   - We take the absolute value of the difference to ensure it is always positive.

3. **Algorithm:**
   - Initialize a variable to keep track of the score.
   - Iterate through the string from the first character to the second-last character.
   - For each pair of adjacent characters, calculate the absolute difference of their ASCII values and add it to the score.
   - Return the total score.

Look at each pair of neighboring letters in the string. For each pair, find out how different the letters are by subtracting their numbers. We add up all these differences to get the total score.

Here is the Python code implementing the solution:

```python
class Solution(object):
    def scoreOfString(self, s):
        """
        :type s: str
        :rtype: int
        """
        
```

## Usage

To use the solution, create an instance of the `Solution` class and call the `scoreOfString` method with the string `s`:

```python
solution = Solution()
s = "abcd"
result = solution.scoreOfString(s)
print(result)  # Output: 3
```


[Link to detailed explanation on Medium](https://medium.com/@trinadhrayala/3110-score-of-a-string-35c8cfdd4bd7)

[Link to detailed explanation on Geeksforgeeks](https://www.geeksforgeeks.org/python-extract-score-list-of-string/)



## Check Out this video

[![Video Explanation](https://img.youtube.com/vi/imbrLFL20tQ/mqdefault.jpg)](https://youtu.be/imbrLFL20tQ)

## Complexity Analysis

- **Time Complexity:** O(n), where n is the length of the string `s`. We iterate through the string once to calculate the score.
- **Space Complexity:** O(1), as we are using a constant amount of extra space to store the score.