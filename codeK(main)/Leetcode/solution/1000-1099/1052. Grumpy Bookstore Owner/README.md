# Leetcode - Grumpy Bookstore Owner

## Problem Description

There is a bookstore owner that has a store open for `n` minutes. Every minute, some number of customers enter the store. You are given an integer array `customers` of length `n` where `customers[i]` is the number of customers that enter the store at the start of the `i-th` minute and all those customers leave after the end of that minute.

On some minutes, the bookstore owner is grumpy. You are given a binary array `grumpy` where `grumpy[i]` is `1` if the bookstore owner is grumpy during the `i-th` minute, and is `0` otherwise.

When the bookstore owner is grumpy, the customers of that minute are not satisfied; otherwise, they are satisfied.

The bookstore owner knows a secret technique to keep themselves not grumpy for `minutes` consecutive minutes, but can only use it once.

Return *the maximum number of customers that can be satisfied throughout the day*.

**Constraints:**
- `n == customers.length == grumpy.length`
- `1 <= minutes <= n <= 2 * 10^4`
- `0 <= customers[i] <= 1000`
- `grumpy[i]` is either `0` or `1`

## Solution

To maximize the number of satisfied customers, consider using the secret technique optimally.

1. **Understanding the Problem:**
   - Maximize the number of satisfied customers.
   - Customers are satisfied when the owner is not grumpy.
   - We can use a technique to prevent the owner from being grumpy for `minutes` consecutive minutes, but only once.

2. **Using a Sliding Window Approach:**
   - Calculate the number of satisfied customers without using the technique.
   - Use a sliding window of size `minutes` to determine the maximum additional satisfied customers when applying the technique.

3. **Algorithm Steps:**
   - Calculate the total number of satisfied customers when the owner is not grumpy.
   - Use a sliding window to find the maximum number of additional customers that can be satisfied by using the technique.
   - Add the additional satisfied customers to the initial satisfied customers to get the maximum number.

### Example

Suppose you have `customers = [1, 0, 1, 2, 1, 1, 7, 5]` and `grumpy = [0, 1, 0, 1, 0, 1, 0, 1]`, and `minutes = 3`.

1. Calculate the initially satisfied customers:
   - Satisfied customers = 1 (minute 0) + 1 (minute 2) + 1 (minute 4) + 7 (minute 6) = 10.
2. Use a sliding window to find the additional satisfied customers:
   - From minute 0 to 2: 0 + 1 + 2 = 3
   - From minute 1 to 3: 1 + 2 + 1 = 4
   - From minute 2 to 4: 1 + 2 + 1 = 4
   - From minute 3 to 5: 2 + 1 + 1 = 4
   - From minute 4 to 6: 1 + 1 + 7 = 9
   - From minute 5 to 7: 1 + 7 + 5 = 13
3. The maximum additional satisfied customers = 13.
4. Total satisfied customers = 10 + 13 = 23.

### Python Code


```python
class Solution(object):
    def maxSatisfied(self, customers, grumpy, minutes):
        """
        :type customers: List[int]
        :type grumpy: List[int]
        :type minutes: int
        :rtype: int
        """
        
```

### Usage

To use the solution, create an instance of the `Solution` class and call the `maxSatisfied` method with `customers`, `grumpy`, and `minutes`:

```python
solution = Solution()
customers = [1, 0, 1, 2, 1, 1, 7, 5]
grumpy = [0, 1, 0, 1, 0, 1, 0, 1]
minutes = 3
result = solution.maxSatisfied(customers, grumpy, minutes)
print(result)  # Output: 23
```

### Additional Resources

[Link to detailed explanation on Algo Monster](https://algo.monster/liteproblems/1052)

### Check Out These Videos

[![Video Explanation](https://img.youtube.com/vi/pXFbNuEIn8Q/mqdefault.jpg)](https://youtu.be/pXFbNuEIn8Q)

[![Video Explanation](https://img.youtube.com/vi/2vI0VpxlOHM/mqdefault.jpg)](https://youtu.be/2vI0VpxlOHM)

[![Video Explanation](https://img.youtube.com/vi/QF1CEMgdRG4/mqdefault.jpg)](https://youtu.be/QF1CEMgdRG4)

### Complexity Analysis

- **Time Complexity:** O(n), where `n` is the number of minutes. The complexity is dominated by the sliding window operation.
- **Space Complexity:** O(1), since no additional space proportional to the input size is required. The calculations are performed in-place.