# Leetcode - Sum of Square Numbers

## Problem Description

Given a non-negative integer `c`, decide whether there are two integers `a` and `b` such that `\( a^2 + b^2 = c \).`

**Constraints:**
- `0 <= c <= 2^31 - 1`

## Solution

To determine if there exist two integers `a` and `b` such that \( a^2 + b^2 = c \):

1. **Understanding the Problem:**
   - Check if the given number `c` can be expressed as the sum of squares of two integers.
   - This involves finding two numbers `a` and `b` such that \( a^2 + b^2 = c \).

2. **Using the Two-Pointer Technique:**
   - Use two pointers: one starting from 0 and the other starting from the largest possible integer whose square is less than or equal to `c`.
   - By adjusting these pointers, we can check all possible pairs of `a` and `b`.

3. **Algorithm Steps:**
   - Initialize two pointers: `left` to 0 and `right` to \( \sqrt{c} \).
   - While `left` is less than or equal to `right`:
     - Calculate the current sum of squares: `current_sum = left^2 + right^2`.
     - If `current_sum` is equal to `c`, return `True`.
     - If `current_sum` is less than `c`, increment `left`.
     - If `current_sum` is greater than `c`, decrement `right`.
   - If no pair is found, return `False`.

### Example

Suppose you have `c = 5`.

1. Initialize `left = 0` and `right = 2` (since \( \sqrt{5} \approx 2.24 \)).
2. Check the sum of squares:
   - \( 0^2 + 2^2 = 4 \) (less than 5), increment `left` to 1.
   - \( 1^2 + 2^2 = 5 \) (equal to 5), return `True`.

### Python Code

Here’s how you can implement this solution in Python:

```python
class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """

```

### Usage

To use the solution, create an instance of the `Solution` class and call the `judgeSquareSum` method with `c`:

```python
solution = Solution()
c = 5
result = solution.judgeSquareSum(c)
print(result)  # Output: True
```

### Additional Resources

[Link to detailed explanation on GeeksforGeeks](https://www.geeksforgeeks.org/how-to-calculate-the-sum-of-squares/)

[Link to detailed explanation on Medium](https://medium.com/@everythingismindgame/633-sum-of-square-numbers-9e537748852a)

[Link to detailed explanation on AlgoMonster](https://algo.monster/liteproblems/633)

### Check Out These Videos

[![Video Explanation](https://img.youtube.com/vi/B0UrG_X2faA/mqdefault.jpg)](https://youtu.be/B0UrG_X2faA)

[![Video Explanation](https://img.youtube.com/vi/fRK4jGPmblc/mqdefault.jpg)](https://youtu.be/fRK4jGPmblc)

[![Video Explanation](https://img.youtube.com/vi/DlQQMXlMxFQ/mqdefault.jpg)](https://youtu.be/DlQQMXlMxFQ)


### Complexity Analysis

- **Time Complexity:** O(\( \sqrt{c} \)), where `c` is the input integer. The complexity is dominated by the iteration through the possible values of `a` and `b`.
- **Space Complexity:** O(1), since no additional space proportional to the input size is required. The calculations are performed in-place.