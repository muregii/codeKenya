# Leetcode - Three Consecutive Odds

## Problem Description

Given an integer array `arr`, return `true` if there are three consecutive odd numbers in the array. Otherwise, return `false`.

**Constraints:**
- `1 <= arr.length <= 1000`
- `1 <= arr[i] <= 1000`

## Solution

To determine if there are three consecutive odd numbers in the array, iterate through the array and check for sequences of three consecutive elements that are all odd numbers.

1. **Understanding the Problem:**
   - Check if there are any three consecutive elements in the array that are odd.
   - An odd number is an integer that is not divisible by 2.

2. **Iterative Approach:**
   - Traverse the array and check each triplet of consecutive elements.
   - For each triplet, check if all three numbers are odd.

3. **Algorithm Steps:**
   - Initialize a counter to keep track of consecutive odd numbers.
   - Iterate through the array from the start to the end.
   - If an element is odd, increment the counter.
   - If an element is even, reset the counter to zero.
   - If the counter reaches three, return `true` as we have found three consecutive odd numbers.
   - If the iteration completes without finding three consecutive odd numbers, return `false`.

### Example

Suppose you have the following array:

```
arr = [2, 6, 4, 1, 3, 5]
```

- Iterate through the array:
  - 2 is even, reset counter to 0.
  - 6 is even, reset counter to 0.
  - 4 is even, reset counter to 0.
  - 1 is odd, increment counter to 1.
  - 3 is odd, increment counter to 2.
  - 5 is odd, increment counter to 3.

- Since the counter reached 3, return `true`.

### Python Code

```python
class Solution(object):
    def threeConsecutiveOdds(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        
```

### Usage

To use the solution, create an instance of the `Solution` class and call the `threeConsecutiveOdds` method with the array:

```python
solution = Solution()
arr = [2, 6, 4, 1, 3, 5]
result = solution.threeConsecutiveOdds(arr)
print(result)  # Output: True
```

### Additional Resources

[Link to detailed explanation on Algo Monster](https://algo.monster/liteproblems/1550)

[Link to detailed explanation on Medium](https://medium.com/@1chooo/leetcode-1550-three-consecutive-odds-go-7a157a76fcd0)



### Check Out These Videos

[![Video Explanation](https://img.youtube.com/vi/ErtxmIdMCf0/mqdefault.jpg)](https://youtu.be/ErtxmIdMCf0)

### Complexity Analysis

- **Time Complexity:** O(n), where `n` is the length of the array. We traverse the array once.
- **Space Complexity:** O(1), as we are using only a constant amount of extra space for the counter.