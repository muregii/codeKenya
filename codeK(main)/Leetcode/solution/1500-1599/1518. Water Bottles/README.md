# Leetcode - Maximum Number of Water Bottles

## Problem Description

There are `numBottles` water bottles that are initially full of water. You can exchange `numExchange` empty water bottles from the market with one full water bottle. The operation of drinking a full water bottle turns it into an empty bottle.

Given the two integers `numBottles` and `numExchange`, return *the **maximum** number of water bottles you can drink*.

**Constraints:**
- `1 <= numBottles <= 100`
- `2 <= numExchange <= 100`

## Solution

To determine the maximum number of water bottles you can drink, simulate the process of drinking and exchanging water bottles until you can no longer exchange empty bottles for full ones.

1. **Understanding the Problem:**
   - Each full water bottle you drink becomes an empty bottle.
   - You can exchange `numExchange` empty bottles for one full bottle.
   - Continue drinking and exchanging until you can no longer get full bottles from exchanges.

2. **Simulating the Process:**
   - Track the total number of bottles drunk.
   - Continuously exchange empty bottles for full bottles as long as possible.

3. **Algorithm Steps:**
   - Initialize the total count of bottles drunk with `numBottles`.
   - While you have enough empty bottles to exchange for at least one full bottle:
     - Exchange empty bottles for full bottles.
     - Drink the newly acquired full bottles and update the total count and number of empty bottles.
   - Return the total count of bottles drunk.

### Example

Suppose you have `numBottles = 9` and `numExchange = 3`:

- Initial full bottles: 9
- Drink 9 bottles, resulting in 9 empty bottles.
- Exchange 9 empty bottles for 3 full bottles (3 exchanges of 3 empty bottles).
- Drink 3 full bottles, resulting in 3 empty bottles.
- Exchange 3 empty bottles for 1 full bottle (1 exchange of 3 empty bottles).
- Drink 1 full bottle, resulting in 1 empty bottle.
- No more exchanges possible.

The result is 13 (9 + 3 + 1) bottles.

### Python Code

```python
class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        """

```

### Usage

To use the solution, create an instance of the `Solution` class and call the `numWaterBottles` method with the number of initial bottles and the exchange rate:

```python
# Example usage
solution = Solution()
numBottles = 9
numExchange = 3
result = solution.numWaterBottles(numBottles, numExchange)
print(result)  # Output: 13
```

### Additional Resources

[Link to detailed explanation on Algo Monster](https://algo.monster/liteproblems/1518)

[Link to detailed explanation on Medium](https://medium.com/@yy929058/leetcode-1518-water-bottles-193ba5261861)

### Check Out These Videos

[![Video Explanation](https://img.youtube.com/vi/V4d6xym5efE/mqdefault.jpg)](https://youtu.be/V4d6xym5efE)

[![Video Explanation](https://img.youtube.com/vi/7CIh3omq_ns/mqdefault.jpg)](https://youtu.be/7CIh3omq_ns)

[![Video Explanation](https://img.youtube.com/vi/BCRV8JIyj3k/mqdefault.jpg)](https://youtu.be/BCRV8JIyj3k)

### Complexity Analysis

- **Time Complexity:** O(log(numBottles)), because the number of bottles decreases geometrically with each exchange.
- **Space Complexity:** O(1), as we only use a constant amount of extra space.