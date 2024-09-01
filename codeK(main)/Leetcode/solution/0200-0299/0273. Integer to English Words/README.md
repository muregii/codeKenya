# Leetcode - Integer to English Words

## Problem Description

Convert a non-negative integer `num` to its English words representation.

For example:
- `123` should be converted to `"One Hundred Twenty Three"`.
- `12345` should be converted to `"Twelve Thousand Three Hundred Forty Five"`.
- `1234567` should be converted to `"One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"`.

**Constraints:**
- `0 <= num <= 2^31 - 1`

## Solution

**Understanding the Problem:**
   - The task is to convert a given integer into its equivalent English words.
   - This requires breaking down the number into smaller segments (thousands, millions, etc.) and converting each segment into words.
   - We will need to handle special cases such as numbers less than 20 and multiples of 10 separately, as they have unique names in English.

**Breaking It Down**
   - **Basic Number Segments:**
     - Numbers from `1` to `19` have unique names (`One`, `Two`, ..., `Nineteen`).
     - Multiples of `10` from `20` to `90` also have unique names (`Twenty`, `Thirty`, ..., `Ninety`).
     
   - **Grouping Numbers:**
     - Numbers are grouped in sets of three digits (hundreds, thousands, millions, etc.).
     - For each group of three digits, we convert them into words and append the corresponding scale word (`Thousand`, `Million`, `Billion`).

   - **Handling Zero:**
     - If `num` is `0`, the output should be `"Zero"`.

**Implementation Approach:**
   - Define arrays for basic numbers (`1-19`) and tens (`20, 30, ..., 90`).
   - Recursively break down the number into its segments (hundreds, thousands, etc.) and convert each segment into words.
   - Combine the segments to form the final word representation.

**Algorithm Steps:**
   - **Edge Case:** If `num` is `0`, return `"Zero"`.
   - **Recursive Conversion:** Define a helper function to convert numbers less than `1000` into words.
   - **Segment the Number:** Break down the number into segments of three digits and convert each segment.
   - **Combine Words:** Assemble the words for each segment and append the corresponding scale (thousand, million, etc.).
   - **Return the Result:** Join the words with spaces and return the final string.

### Python Code

```python
class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        
```

### Example

```python
# Input
num = 1234567

# Output
"One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
```

### Explanation
1. **Segment the Number:** 
   - The number `1234567` is broken down into `1 Million`, `234 Thousand`, and `567`.
2. **Convert Segments:** Each segment is converted into its word form and combined.
3. **Result:** The final result is `"One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"`.

### Usage

To use the solution, create an instance of the `Solution` class and call the `numberToWords` method with the `num` integer:

```python
# Example usage
solution = Solution()
num = 1234567
result = solution.numberToWords(num)
print(result)  # Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
```

### Additional Resources

[Link to detailed explanation on Algo Monster](https://algo.monster/liteproblems/273)

[Link to detailed explanation on Medium](https://nishantt.medium.com/integer-to-english-words-leetcode-273-f16c5e1b50eb)

### Check Out These Video(s)

[![Video Explanation](https://img.youtube.com/vi/JEz9jXxWavo/mqdefault.jpg)](https://youtu.be/JEz9jXxWavo)

[![Video Explanation](https://img.youtube.com/vi/vLq_4DIfRIM/mqdefault.jpg)](https://youtu.be/vLq_4DIfRIM)

[![Video Explanation](https://img.youtube.com/vi/SCtIlKd3mDM/mqdefault.jpg)](https://youtu.be/SCtIlKd3mDM)

### Complexity Analysis

- **Time Complexity:** O(1), as the number has a constant number of digits.
- **Space Complexity:** O(1), as we are only using a few extra variables for the conversion process.