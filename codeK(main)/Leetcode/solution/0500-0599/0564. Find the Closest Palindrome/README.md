# Leetcode - Find the Closest Palindrome

## Problem Description

Given a string `n` representing an integer, return *the **closest** integer (not including itself), which is a palindrome. If there is a tie, return the **smaller one**.*

The closest is defined as the absolute difference minimized between two integers.

 

### Constraints:
- `1 <= n.length <= 18`
- `n` consists of only digits.
- `n` does not have leading zeros.
- `n` is representing an integer in the range [1, 10^18 - 1].

## Solution

**Understanding the Problem:**
- We need to find the closest palindrome number to the given string `n`. A palindrome is a number that reads the same forwards and backwards (e.g., `121`, `909`, `88`).
- The challenge is to identify the closest palindrome and return the smaller one in case of a tie.
- We can approach this problem by generating several possible palindrome candidates and selecting the one closest to `n`.

**Breaking It Down:**
- **Generating Palindromes:** Since the palindrome must be close to the input `n`, we can generate palindromes by manipulating the first half of `n` and mirroring it. We will consider three key cases:
  1. Palindrome derived from the middle digits of `n`.
  2. Palindrome by slightly decreasing the first half of `n`.
  3. Palindrome by slightly increasing the first half of `n`.
- **Edge Cases:** Handle special cases such as:
  - Numbers like `1000`, where the closest palindrome is `999`.
  - Single-digit numbers, where the nearest palindrome is always `n-1`.

**Implementation Approach:**
1. **Base Case:** If the input `n` has only one digit, return `n-1` since all single-digit palindromes are the numbers themselves.
2. **Generate Candidate Palindromes:**
   - Create palindromes by reversing and mirroring the first half of `n`.
   - Consider decreasing and increasing the first half to account for smaller and larger palindrome possibilities.
3. **Compute Closest Palindrome:**
   - Calculate the absolute difference between each generated palindrome and the original number `n`.
   - Return the palindrome with the smallest absolute difference, and in case of a tie, return the smaller palindrome.

**Algorithm Steps:**
1. **Identify Key Candidates:** Use the first half of `n` to create three palindrome candidates:
   - The middle palindrome.
   - The smaller palindrome (slightly reduced version).
   - The larger palindrome (slightly increased version).
2. **Handle Edge Cases:** Handle cases like numbers ending in zeros, or single-digit numbers where the answer is trivially `n-1`.
3. **Compare Candidates:** Compare all palindrome candidates and return the one closest to `n` by absolute difference.

### Python Code

```python
class Solution(object):
    def nearestPalindromic(self, n):
        """
        :type n: str
        :rtype: str
        """
        
```

### Example

```python
# Input
n = "123"

# Output
"121"
```

### Explanation

1. **Generating Palindromes:**
   - For the input `n = "123"`, the first half is `12`.
   - Possible palindromes are: `"121"` (same size), `"111"` (smaller), and `"131"` (larger).
2. **Compute Closest Palindrome:**
   - Compare the candidates and their absolute difference from `123`. The closest is `"121"`, which has an absolute difference of `2`.

### Usage

To use the solution, create an instance of the `Solution` class and call the `nearestPalindromic` method with the input string `n`:

```python
# Example usage
solution = Solution()
n = "123"
result = solution.nearestPalindromic(n)
print(result)  # Output: "121"
```

### Additional Resources

[Link to detailed explanation on Algo Monster](https://algo.monster/liteproblems/564)

[Link to detailed explanation on Medium](https://dreamume.medium.com/leetcode-564-find-the-closest-palindrome-c5661c8d7411)

[Link to detailed explanation on Geeksforgeeks](https://www.geeksforgeeks.org/closest-palindrome-number-whose-absolute-difference-min/)

### Check Out These Video(s)

[![Video Explanation](https://img.youtube.com/vi/vJBlA5y4q3w/mqdefault.jpg)](https://youtu.be/vJBlA5y4q3w)


### Complexity Analysis

- **Time Complexity:** O(n), where `n` is the length of the string `n`. The palindrome generation and comparison steps run in linear time relative to the length of the input.
- **Space Complexity:** O(n), for storing the palindrome candidates and performing the calculations based on string manipulations.