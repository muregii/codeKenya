# Leetcode - Maximum Profit Assignment

## Problem Description

You have `n` jobs and `m` workers. You are given three arrays: `difficulty`, `profit`, and `worker` where:

- `difficulty[i]` and `profit[i]` are the difficulty and the profit of the `ith` job.
- `worker[j]` is the ability of the `jth` worker (i.e., the `jth` worker can only complete a job with difficulty at most `worker[j]`).

Every worker can be assigned at **most one job**, but one job can be **completed multiple times**. 
- For example, if three workers attempt the same job that pays `$1`, then the total profit will be `$3`. If a worker cannot complete any job, their profit is `$0`. 

Return the maximum profit we can achieve after assigning the workers to the jobs.

**Constraints:**
- `n == difficulty.length`
- `n == profit.length`
- `m == worker.length`
- `1 <= n, m <= 10^4`
- `1 <= difficulty[i], profit[i], worker[i] <= 10^5`

## Solution

To maximize the total profit from assigning jobs to workers, match each worker with the most profitable job they can complete.

1. **Understanding the Problem:**
   - Assign jobs to workers based on their abilities and maximize the profit.
   - Each worker can only do jobs whose difficulty is less than or equal to their ability.
   - Each worker can be assigned at most one job, but each job can be completed by multiple workers.

2. **Using a Sorting and Binary Search Approach:**
   - Sort the jobs based on their difficulty.
   - Sort the workers based on their ability.
   - For each worker, use binary search to find the most profitable job they can do.

3. **Algorithm Steps:**
   - Sort the `difficulty` and `profit` arrays based on the difficulty of the jobs.
   - Sort the `worker` array based on the ability of the workers.
   - Iterate through each worker and find the best job they can do using a pointer to keep track of the maximum profit job they can handle.
   - Accumulate the total profit based on the jobs assigned to the workers.

### Example

Suppose you have `difficulty = [2, 4, 6, 8]`, `profit = [10, 20, 30, 40]`, and `worker = [5, 6, 7, 8]`.

1. Sort `difficulty` and `profit` arrays:
   - `difficulty = [2, 4, 6, 8]`
   - `profit = [10, 20, 30, 40]`
2. Sort `worker` array:
   - `worker = [5, 6, 7, 8]`
3. Assign jobs to workers:
   - Worker with ability 5 can do jobs with difficulty up to 4, so they get a profit of 20.
   - Worker with ability 6 can do jobs with difficulty up to 6, so they get a profit of 30.
   - Worker with ability 7 can do jobs with difficulty up to 6, so they get a profit of 30.
   - Worker with ability 8 can do jobs with difficulty up to 8, so they get a profit of 40.
4. Total profit: `20 + 30 + 30 + 40 = 120`.

### Python Code


```python
class Solution(object):
    def maxProfitAssignment(self, difficulty, profit, worker):
        """
        :type difficulty: List[int]
        :type profit: List[int]
        :type worker: List[int]
        :rtype: int
        """
        
```

### Usage

To use the solution, create an instance of the `Solution` class and call the `maxProfitAssignment` method with `difficulty`, `profit`, and `worker`:

```python
solution = Solution()
difficulty = [2, 4, 6, 8]
profit = [10, 20, 30, 40]
worker = [5, 6, 7, 8]
result = solution.maxProfitAssignment(difficulty, profit, worker)
print(result)  # Output: 120
```

### Additional Resources

[Link to detailed explanation on Medium](https://medium.com/@codingQueen98/leetcode-826-most-profit-assigning-work-java-solution-aa6931995e62)

[Link to detailed explanation on AlgoMonster](https://algo.monster/liteproblems/826)

### Check Out These Videos

[![Video Explanation](https://img.youtube.com/vi/V-gYS2b8Ux0/mqdefault.jpg)](https://youtu.be/V-gYS2b8Ux0)

[![Video Explanation](https://img.youtube.com/vi/vL6ZbaP9API/mqdefault.jpg)](https://youtu.be/vL6ZbaP9API)

### Complexity Analysis

- **Time Complexity:** O(n log n + m log m), where `n` is the number of jobs and `m` is the number of workers. The complexity is dominated by the sorting operations.
- **Space Complexity:** O(n + m), since we store the sorted lists and iterate through them.