# Leetcode - Pass the Pillow

## Problem Description

There are `n` people standing in a line labeled from 1 to `n`. The first person in the line is holding a pillow initially. Every second, the person holding the pillow passes it to the next person standing in the line. Once the pillow reaches the end of the line, the direction changes, and people continue passing the pillow in the opposite direction.

- For example, once the pillow reaches the `n`th person they pass it to the `n-1`th person, then to the `n-2`th person, and so on.

Given the two positive integers `n` and `time`, return *the index of the person holding the pillow after `time` seconds*.

**Constraints:**
- `2 <= n <= 1000`
- `1 <= time <= 1000`

## Solution

To determine who is holding the pillow after a given time, simulate the movement of the pillow back and forth along the line. 

1. **Understanding the Problem:**
   - The pillow moves forward until it reaches the end of the line, then reverses direction.
   - We need to determine the position of the pillow after a given number of seconds.

2. **Simulating the Movement:**
   - Track the direction of the pillow's movement.
   - Use modulo arithmetic to determine the final position after the given time.

3. **Algorithm Steps:**
   - Calculate the total effective movements by using modulo arithmetic with `n-1`.
   - Determine the final position based on the direction of movement.

### Example

Suppose you have `n = 5` people and the time is `7` seconds:

- Initial positions: `1 -> 2 -> 3 -> 4 -> 5`
- After 1 second: `2`
- After 2 seconds: `3`
- After 3 seconds: `4`
- After 4 seconds: `5`
- After 5 seconds: `4` (reverse direction)
- After 6 seconds: `3`
- After 7 seconds: `2`

The result is `2`.

### Python Code

```python
class Solution(object):
    def passThePillow(self, n, time):
        """
        :type n: int
        :type time: int
        :rtype: int
        """
        
```

### Usage

To use the solution, create an instance of the `Solution` class and call the `passThePillow` method with the number of people and the time:

```python
# Example usage
solution = Solution()
n = 5
time = 7
result = solution.passThePillow(n, time)
print(result)  # Output: 2
```

### Additional Resources

[Link to detailed explanation on Algo Monster](https://algo.monster/liteproblems/2582)

### Check Out These Videos

[![Video Explanation](https://img.youtube.com/vi/gPUSB5u9zbA/mqdefault.jpg)](https://youtu.be/gPUSB5u9zbA)

### Complexity Analysis

- **Time Complexity:** O(1), because we calculate the result using a few arithmetic operations.
- **Space Complexity:** O(1), as we only use a constant amount of extra space.