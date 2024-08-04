# Leetcode - Average Waiting Time

## Problem Description

There is a restaurant with a single chef. You are given an array `customers`, where `customers[i] = [arrival_i, time_i]`:

- `arrival_i` is the arrival time of the `i`th customer. The arrival times are sorted in **non-decreasing** order.
- `time_i` is the time needed to prepare the order of the `i`th customer.

When a customer arrives, he gives the chef his order, and the chef starts preparing it once he is idle. The customer waits till the chef finishes preparing his order. The chef does not prepare food for more than one customer at a time. The chef prepares food for customers in the order they were given in the input.

Return *the **average** waiting time of all customers*. Solutions within `10^-5` from the actual answer are considered accepted.

**Constraints:**
- `1 <= customers.length <= 10^5`
- `1 <= arrival_i, time_i <= 10^4`
- `arrival_i <= arrival_{i+1}`

## Solution

To determine the average waiting time of all customers, simulate the process of the chef preparing orders and calculate the waiting time for each customer.

1. **Understanding the Problem:**
   - Each customer waits from their arrival time until the chef finishes preparing their order.
   - The chef prepares orders one at a time in the given order of arrivals.

2. **Simulating the Process:**
   - Track the current time when the chef finishes the last order.
   - For each customer, calculate their waiting time based on the current time and their arrival time.
   - Update the current time after the chef finishes each order.

3. **Algorithm Steps:**
   - Initialize the current time and total waiting time.
   - Iterate through each customer, updating the current time and calculating their waiting time.
   - Return the average waiting time by dividing the total waiting time by the number of customers.

### Example

Suppose you have `customers = [[1, 2], [2, 5], [4, 3]]`:

- Customer 1 arrives at time 1 and needs 2 units of time.
- Customer 2 arrives at time 2 and needs 5 units of time.
- Customer 3 arrives at time 4 and needs 3 units of time.

Processing the customers:
1. Customer 1 arrives at time 1 and waits until time 3 (1+2), waiting time = 2.
2. Customer 2 arrives at time 2, starts at time 3, finishes at time 8 (3+5), waiting time = 6.
3. Customer 3 arrives at time 4, starts at time 8, finishes at time 11 (8+3), waiting time = 7.

Total waiting time = 2 + 6 + 7 = 15. Average waiting time = 15 / 3 = 5.

### Python Code

```python
class Solution(object):
    def averageWaitingTime(self, customers):
        """
        :type customers: List[List[int]]
        :rtype: float
        """
        
```

### Usage

To use the solution, create an instance of the `Solution` class and call the `averageWaitingTime` method with the list of customers:

```python
# Example usage
solution = Solution()
customers = [[1, 2], [2, 5], [4, 3]]
result = solution.averageWaitingTime(customers)
print(result)  # Output: 5.0
```

### Additional Resources

[Link to detailed explanation on Algo Monster](https://algo.monster/liteproblems/1701)

[Link to detailed explanation on Medium](https://medium.com/@everythingismindgame/1701-average-waiting-time-rust-go-cpp-33c129106e17)

[Link to detailed explanation on Medium](https://medium.com/@trinadhrayala/leetcode-daily-challenge-1701-average-waiting-time-acd53263b9fa)

### Check Out These Videos

[![Video Explanation](https://img.youtube.com/vi/2fN7uIgCIBA/mqdefault.jpg)](https://youtu.be/2fN7uIgCIBA)

[![Video Explanation](https://img.youtube.com/vi/MhY6x3h0t3o/mqdefault.jpg)](https://youtu.be/MhY6x3h0t3o)

### Complexity Analysis

- **Time Complexity:** O(n), as we iterate through the list of customers once.
- **Space Complexity:** O(1), as we use a constant amount of extra space.