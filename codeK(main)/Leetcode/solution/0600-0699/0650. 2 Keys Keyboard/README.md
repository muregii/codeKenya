# Leetcode - 2 Keys Keyboard

## Problem Description

There is only one character `'A'` on the screen of a notepad. You can perform one of two operations on this notepad for each step:

1. **Copy All**: Copy all the characters currently on the screen (partial copies are not allowed).
2. **Paste**: Paste the characters that were last copied.

Given an integer `n`, return *the minimum number of operations to get the character `'A'` exactly n times on the screen.*

**Constraints:**
- `1 <= n <= 1000`

## Solution

**Understanding the Problem:**

To get exactly `n` 'A' characters on the screen, we need to find the most efficient way to use the **Copy All** and **Paste** operations. The key insight here is that we should try to maximize the number of characters pasted in each step, which can be achieved by finding the factors of `n`.

At every step, we can either **copy** all characters or **paste** the previously copied characters. The trick is to realize that we can break down the problem into factors: if `n` is divisible by some number, we can reduce the problem to solving it for a smaller number of 'A's.

For example:
- If `n = 6`, one efficient strategy is to copy 2 'A's and paste them twice to get 4 'A's, then copy 4 and paste them once to reach 6 'A's.
- If `n = 9`, you can copy 3 'A's and paste them twice to reach 9 'A's.

**Breaking It Down:**

- If `n` is divisible by `k`, we can copy the result of `n/k` steps and paste it `k` times.
- The goal is to minimize the number of operations by using the largest factors of `n`.

**Implementation Approach:**

- Use **dynamic programming** or a **greedy approach** to find the minimum number of steps required by identifying the factors of `n`.
- For each divisor `k`, compute how many operations are needed by reducing the problem to smaller values of `n`.

**Algorithm Steps:**

1. **Factorization Strategy:**
   - Start from `n` and find the smallest divisor `k` (except 1).
   - Divide `n` by `k` and recursively solve for the smaller number.
   - Each time we find a divisor, we count the operations as the divisor `k` (since we need `k` paste operations after a copy).
   
2. **Iterate Over Factors:** For each factor of `n`, add the number of operations required (which is the factor itself) and repeat until we reach 1.

### Python Code

```python
class Solution(object):
    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """
        
```

### Example

```python
# Input
n = 6

# Output
5
```

### Explanation

1. Start with one 'A' on the screen.
2. Copy All, then Paste 2 times (to get 4 'A's).
3. Copy All, then Paste 1 time (to get 6 'A's).

This requires 5 operations in total.

### Usage

To use the solution, create an instance of the `Solution` class and call the `minSteps` method with the `n` parameter:

```python
# Example usage
solution = Solution()
n = 6
result = solution.minSteps(n)
print(result)  # Output: 5
```

### Additional Resources

[Link to detailed explanation on Algo Monster](https://algo.monster/liteproblems/650)


### Check Out These Video(s)

[![Video Explanation](https://img.youtube.com/vi/CIDdvpX66IY/mqdefault.jpg)](https://youtu.be/CIDdvpX66IY)

[![Video Explanation](https://img.youtube.com/vi/jNfZH3mdjOA/mqdefault.jpg)](https://youtu.be/jNfZH3mdjOA)

### Complexity Analysis

- **Time Complexity:** O(sqrt(n)), where `n` is the input number. This is because we only need to check divisors up to `sqrt(n)` during factorization.
- **Space Complexity:** O(1), as we are only using a few variables for the factorization process.