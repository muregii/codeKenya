# Leetcode - Palindrome Partitioning

## Problem Description

Given a string `s`, partition `s` such that every **substring** of the partition is a **palindrome**. Return *all possible palindrome partitioning of `s`.*

**Constraints:**
- `1 <= s.length <= 16`
- `s` contains only lowercase English letters.

## Solution

Generate all possible partitions of the string `s` such that each partition is a palindrome.

Think of a word like a big cake. We want to cut the cake into pieces, but the rule is that each piece has to be a palindrome. A palindrome is a word that reads the same forward and backward, like 'madam' or 'racecar'. We need to find all possible ways to cut the cake so that every piece is a palindrome.


The `partition` method takes a string `s` and returns all possible palindrome partitions of `s`.

1. **Checking for Palindromes:**
   - A helper function `is_palindrome` checks if a substring is a palindrome by comparing characters from both ends.

2. **Generating Partitions:**
   - Use a recursive approach with a helper function `dfs` to generate all partitions.
   - For each starting position in the string, check every possible end position.
   - If the substring is a palindrome, include it in the current partition and recursively generate partitions for the remaining substring.

3. **Algorithm:**
   - Use the `dfs` function to explore all possible partitions.
   - Start with an empty partition and iterate through the string, adding each palindrome substring to the current partition and exploring further combinations recursively.


We start with an empty list and look at each part of the word. For each part, we check if it's a palindrome. If it is, we include it in our current group of pieces and continue to look for more palindromes in the remaining part of the word. We do this until we've considered every possible way to cut the word into palindromes.


```python

class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        
```

## Usage

To use the solution, create an instance of the `Solution` class and call the `partition` method with the string `s`:

```python
solution = Solution()
s = "aab"
result = solution.partition(s)
print(result)  # Output: [["a","a","b"],["aa","b"]]
```
[Link to detailed explanation on AlgoMonster](https://algo.monster/liteproblems/131)

[Link to detailed explanation on Medium](https://medium.com/@sheefanaaz6417/131-palindrome-partitioning-8ce19c189e94)

[Link to detailed explanation on Geeksforgeeks](https://www.geeksforgeeks.org/given-a-string-print-all-possible-palindromic-partition/)


## Check Out this videos

[![Video Explanation](https://img.youtube.com/vi/3jvWodd7ht0/mqdefault.jpg)](https://youtu.be/3jvWodd7ht0)

[![Video Explanation](https://img.youtube.com/vi/lk1xlGddaAM/mqdefault.jpg)](https://youtu.be/lk1xlGddaAM)

[![Video Explanation](https://img.youtube.com/vi/uJeS6FmbSjM/mqdefault.jpg)](https://youtu.be/uJeS6FmbSjM)

[![Video Explanation](https://img.youtube.com/vi/WBgsABoClE0/mqdefault.jpg)](https://youtu.be/WBgsABoClE0)


## Complexity Analysis

- **Time Complexity:** O(2^n), where n is the length of the string `s`. This is because we are generating all possible partitions.
- **Space Complexity:** O(n), where n is the length of the string `s`. This is the space used by the recursion stack and to store the intermediate results.