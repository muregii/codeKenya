# Leetcode - Strange Printer

## Problem Description

There is a strange printer with the following two special properties:

1. The printer can only print a sequence of the **same character** each time.
2. At each turn, the printer can print new characters starting from and ending at any place, and will cover the original existing characters.

Given a string `s`, return *the minimum number of turns the printer needed to print it*.


### Constraints:
- `1 <= s.length <= 100`
- `s` consists of lowercase English letters.

## Solution

**Understanding the Problem:**
- The strange printer must print a given string, but it can only print a sequence of the same character at a time. We need to determine the minimum number of turns the printer needs to print the string optimally.
- At each turn, the printer prints a segment of the string. If part of the string is already printed, the printer can cover and extend the printed characters. Therefore, the challenge is to minimize the number of print operations by finding overlapping or repetitive segments in the string.

**Breaking It Down:**
- The string has overlapping characters or segments that can be covered in fewer turns. For example:
  - If the string has consecutive identical characters (`"aa"`), we can print them in one turn.
  - For non-consecutive characters, we may need multiple turns.
- **Key Insight:** The problem is similar to dynamic programming (DP) approaches where we optimize operations by calculating subproblems based on previously computed results.

**Dynamic Programming Approach:**
- We can define a DP table `dp[i][j]` where `i` is the starting index and `j` is the ending index of a substring of `s`. `dp[i][j]` stores the minimum number of turns required to print the substring `s[i:j]`.
- For each substring, if the first and last characters are the same, we can potentially minimize the turns required by merging them. Otherwise, we break down the substring into smaller segments and calculate the optimal solution.
  
**Algorithm Steps:**
1. **Base Case:** If `i == j`, the substring is just one character, and we only need 1 turn to print it.
2. **DP Table Initialization:** Initialize a 2D DP table where each entry represents the minimum turns for a substring.
3. **Merge or Divide Substrings:** For each substring `s[i:j]`, if `s[i] == s[j]`, we can merge the printing process. Otherwise, we compute the optimal solution by splitting the substring into two parts and combining the results.
4. **Final Answer:** The value `dp[0][n-1]` (where `n` is the length of `s`) will store the result for the entire string.

### Python Code

```python
class Solution(object):
    def strangePrinter(self, s):
        """
        :type s: str
        :rtype: int
        """
        
```

### Example

```python
# Input
s = "aaabbb"

# Output
2
```

### Explanation
1. For the string `"aaabbb"`, the first three 'a's can be printed in one turn, and the next three 'b's in another turn.
2. Therefore, the minimum number of turns required is `2`.

### Usage

To use the solution, create an instance of the `Solution` class and call the `strangePrinter` method with the input string `s`:

```python
# Example usage
solution = Solution()
s = "aaabbb"
result = solution.strangePrinter(s)
print(result)  # Output: 2
```

### Additional Resources

[Link to detailed explanation on Algo Monster](https://algo.monster/liteproblems/664)

[Link to detailed explanation on Medium](https://medium.com/@_monitsharma/daily-leetcode-problems-problem-664-strange-printer-8629394f20fa)

### Check Out These Video(s)

[![Video Explanation](https://img.youtube.com/vi/fIOZkIH5PZU/mqdefault.jpg)](https://youtu.be/fIOZkIH5PZU)

[![Video Explanation](https://img.youtube.com/vi/yDaWPjVkWk8/mqdefault.jpg)](https://youtu.be/yDaWPjVkWk8)


### Complexity Analysis

- **Time Complexity:** O(n^3), where `n` is the length of the string. This is due to the nested loops that check each substring and try to merge characters.
- **Space Complexity:** O(n^2), for storing the DP table that tracks the minimum turns for each substring.