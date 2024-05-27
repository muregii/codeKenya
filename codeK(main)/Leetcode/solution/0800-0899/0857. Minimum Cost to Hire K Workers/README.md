# Leetcode - Min Cost to Hire K Workers

## Problem Description

There are `n` workers. You are given two integer arrays `quality` and `wage` where `quality[i]` is the quality of the `ith` worker and `wage[i]` is the minimum wage expectation for the `ith` worker.

We want to hire exactly `k` workers to form a paid group. To hire a group of `k` workers, we must pay them according to the following rules:

- Every worker in the paid group must be paid at least their minimum wage expectation.
- In the group, each worker's pay must be directly proportional to their quality. This means if a worker’s quality is double that of another worker in the group, then they must be paid twice as much as the other worker.

Given the integer `k`, *return the least amount of money needed to form a paid group satisfying the above conditions*. Answers within `10^-5` of the actual answer will be accepted.

**Constraints:**

- `n == quality.length == wage.length`
- `1 <= k <= n <= 104`
- `1 <= quality[i], wage[i] <= 104`

## Solution

To solve this problem, we can use a greedy approach with a min-heap to find the minimum cost to hire exactly `k` workers. Here's a step-by-step approach to achieve this:

1. **Calculate Ratios**: For each worker, calculate the ratio of their `wage` to `quality`. This ratio represents the minimum amount we need to pay per unit quality to satisfy this worker's minimum wage requirement.
2. **Sort Workers**: Sort the workers based on their calculated ratio in ascending order. This way, we can consider the cheapest ratio first.
3. **Use a Max-Heap**: Use a max-heap to keep track of the `k` workers with the highest qualities. This helps us ensure that we are selecting the group of `k` workers with the lowest total wage.
4. **Calculate Minimum Cost**: Iterate through the sorted workers and for each worker:
   - Add their quality to the heap.
   - If the heap exceeds `k` workers, remove the worker with the highest quality from the heap (this helps in minimizing the total wage).
   - If the heap size is `k`, calculate the total wage for these workers using the current worker's ratio and update the minimum cost if it is lower than the previous cost.

This method ensures that we always consider the group of `k` workers with the lowest total wage while maintaining the proportional pay condition.

## Usage

To use the solution, create an instance of the `Solution` class and call the `mincostToHireWorkers` method with the input parameters `quality`, `wage`, and `k`:

```python

class Solution(object):
    def mincostToHireWorkers(self, quality, wage, k):
        """
        :type quality: List[int]
        :type wage: List[int]
        :type k: int
        :rtype: float
        """
        
# Example Usage
solution = Solution()
quality = [10, 20, 5]
wage = [70, 50, 30]
k = 2
result = solution.mincostToHireWorkers(quality, wage, k)
print(result)  # Output: 105.00000
```

## Explanation

1. **Input**: The arrays `quality`, `wage`, and integer `k` are given.
2. **Calculate Ratios**: For each worker, calculate the ratio of `wage` to `quality`.
3. **Sort Workers**: Sort the workers based on their calculated ratios in ascending order.
4. **Use Max-Heap**: Use a max-heap to keep track of the top `k` qualities.
5. **Calculate Minimum Cost**: Iterate through the sorted workers, maintaining the heap and calculating the minimum cost when the heap size is `k`.


[Link to detailed explanation on Medium](https://medium.com/@vikasg_65078/leetcode-daily-problem-857-minimum-cost-to-hire-k-workers-may-11-2024-31f95f2c6a29)

[Link to detailed explanation on AlgoMonster](https://algo.monster/liteproblems/857)

## Check Out these videos

[![Video Explanation](https://img.youtube.com/vi/KytaqLXEeJA/mqdefault.jpg)](https://youtu.be/KytaqLXEeJA)

[![Video Explanation](https://img.youtube.com/vi/f879mUH6vJk/mqdefault.jpg)](https://youtu.be/f879mUH6vJk)

## Complexity Analysis

- **Time Complexity:** O(n log n), where n is the number of workers. Sorting the workers takes O(n log n) time, and each heap operation takes O(log k) time.
- **Space Complexity:** O(k), where k is the number of workers we need to hire. The heap will store at most `k` workers at any given time.