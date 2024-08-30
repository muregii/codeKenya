# Leetcode - Minimum Deletions to Make String Balanced

## Problem Description

You are given a string `s` consisting only of characters 'a' and 'b'. 

You can delete any number of characters in `s` to make `s` **balanced**. `s` is **balanced** if there is no pair of indices `(i,j)` such that `i < j` and `s[i] = 'b'` and `s[j]= 'a'`.

Return *the **minimum** number of deletions needed to make `s` **balanced***.

**Constraints:**
- `1 <= s.length <= 10^5`
- `s[i]` is either 'a' or 'b'.

## Solution

**Understanding the Problem:**
   - We are given a string containing only the characters 'a' and 'b'.
   - The string is considered balanced if all 'b's appear before all 'a's.
   - Our goal is to determine the minimum number of deletions required to make the string balanced.

**Breaking It Down**
   - **Identifying Imbalance:**
     - The imbalance occurs when a 'b' appears before an 'a' in the string. To balance the string, we need to delete some characters to ensure that all 'b's come before any 'a's.
     
   - **Optimal Deletion Strategy:**
     - We can iterate through the string and count the minimum number of deletions needed. This can be achieved by keeping track of the number of 'a's that need to be deleted and the number of 'b's that have been encountered so far.
     - As we iterate, if we encounter an 'a' after a 'b', we have two choices: delete the 'a' or delete all preceding 'b's. The optimal solution will minimize the total number of deletions.

**Implementation Approach:**
   - Traverse the string while counting the number of 'b's encountered.
   - For each 'a' that appears after a 'b', consider whether to delete the 'a' or all preceding 'b's.
   - Keep track of the minimum deletions required to balance the string.

**Algorithm Steps:**
   - **Initialize Counters:** Start with counters for the number of 'b's (`count_b`) encountered and the minimum deletions required (`min_deletions`).
   - **Iterate Through the String:** For each character in the string:
     - If it's a 'b', increment the `count_b`.
     - If it's an 'a', calculate the minimum deletions by either deleting this 'a' or deleting all preceding 'b's.
   - **Return Result:** The minimum deletions needed to make the string balanced.

### Python Code

```python
class Solution(object):
    def minimumDeletions(self, s):
        """
        :type s: str
        :rtype: int
        """
        
```

### Example

```python
# Input
s = "aababbab"

# Output
2
```

### Explanation
1. **Initial String:** "aababbab"
2. **Imbalance:** 'b' appears before 'a' at several points.
3. **Minimum Deletions:** The optimal way to balance the string is to delete two 'b's, resulting in "aabaab" which is balanced.

### Usage

To use the solution, create an instance of the `Solution` class and call the `minimumDeletions` method with the `s` string:

```python
# Example usage
solution = Solution()
s = "aababbab"
result = solution.minimumDeletions(s)
print(result)  # Output: 2
```

### Additional Resources

[Link to detailed explanation on Algo Monster](https://algo.monster/liteproblems/1653)

[Link to detailed explanation on Geeksforgeeks](https://www.geeksforgeeks.org/minimum-number-of-additions-to-make-the-string-balanced/)

[Link to detailed explanation on Medium](https://medium.com/@trinadhrayala/leetcode-1653-minimum-deletions-to-make-string-balanced-daily-question-39ba04fef850)

### Check Out These Video(s)

[![Video Explanation](https://img.youtube.com/vi/yMnH0jrir0Q/mqdefault.jpg)](https://youtu.be/yMnH0jrir0Q)

[![Video Explanation](https://img.youtube.com/vi/WDStNufBUQ8/mqdefault.jpg)](https://youtu.be/WDStNufBUQ8)

### Complexity Analysis

- **Time Complexity:** O(n), where `n` is the length of the string `s`. We iterate through the string once.
- **Space Complexity:** O(1), as we only use a few variables to keep track of the count and minimum deletions.