# Leetcode - IPO

## Problem Description

Suppose LeetCode will start its **IPO** soon. In order to sell its shares at a good price to Venture Capital, LeetCode would like to work on some projects to increase its capital before the **IPO**. Since it has limited resources, it can only finish at most `k` distinct projects before the **IPO**. Help LeetCode design the best way to maximize its total capital after finishing at most `k` distinct projects.

You are given `n` projects where the `i-th` project has a pure profit `profits[i]` and a minimum capital `capital[i]` is needed to start it.

Initially, you have `w` capital. When you finish a project, you will obtain its pure profit, and the profit will be added to your total capital.

Pick a list of at **most** `k` distinct projects from the given projects to **maximize your final capital**, and *return the final maximized capital*.

The answer is guaranteed to fit in a 32-bit signed integer.

**Constraints:**
- `1 <= k <= 10^5`
- `0 <= w <= 10^9`
- `n == profits.length`
- `n == capital.length`
- `1 <= n <= 10^5`
- `0 <= profits[i] <= 10^4`
- `0 <= capital[i] <= 10^9`

## Solution

To maximize the total capital after finishing at most `k` distinct projects, we need to prioritize the projects that offer the highest profit and are feasible given the current capital.

1. **Understanding the Problem:**
   - We have an initial capital `w` and need to select at most `k` projects from a list.
   - Each project requires a minimum capital to start and offers a certain profit.
   - The goal is to maximize the final capital after completing the projects.

2. **Using a Priority Queue:**
   - We will use two priority queues (heaps):
     - A min-heap to keep track of projects sorted by their required capital.
     - A max-heap to keep track of the available projects sorted by their profit.

3. **Selection Strategy:**
   - Initially, add all projects that can be started with the initial capital to the max-heap.
   - For each project we can complete (up to `k` projects), select the project with the highest profit (from the max-heap), add its profit to the current capital, and then add new feasible projects to the max-heap based on the updated capital.
   - Repeat this process until we have completed `k` projects or no more feasible projects are left.

### Example

Suppose you have `k = 2`, `w = 0`, `profits = [1, 2, 3]`, and `capital = [0, 1, 1]`.

1. Initialize with `w = 0`:
   - Add projects that can be started with `w = 0` to the max-heap. Only project 0 with profit 1 can be started.
   
2. Select the project with the highest profit from the max-heap:
   - Complete project 0, add its profit to `w`: `w = 0 + 1 = 1`.

3. Update feasible projects:
   - With `w = 1`, add projects that can be started (projects 1 and 2) to the max-heap.

4. Select the project with the highest profit from the max-heap:
   - Complete project 2, add its profit to `w`: `w = 1 + 3 = 4`.

5. Maximum capital after at most 2 projects: `4`.

### Python Code

```python
class Solution(object):
    def findMaximizedCapital(self, k, w, profits, capital):
        """
        :type k: int
        :type w: int
        :type profits: List[int]
        :type capital: List[int]
        :rtype: int
        """
        
```

### Usage

To use the solution, create an instance of the `Solution` class and call the `findMaximizedCapital` method with `k`, `w`, `profits`, and `capital`:

```python
solution = Solution()
k = 2
w = 0
profits = [1, 2, 3]
capital = [0, 1, 1]
result = solution.findMaximizedCapital(k, w, profits, capital)
print(result)  # Output: 4
```

### Additional Resources

[Link to detailed explanation on Medium](https://medium.com/@alessandroamenta1/leetcode-502-ipo-python-9c11ab2bdc00)

[Link to detailed explanation on AlgoMonster](https://algo.monster/liteproblems/502)

### Check Out These Videos

[![Video Explanation](https://img.youtube.com/vi/1IUzNJ6TPEM/mqdefault.jpg)](https://youtu.be/1IUzNJ6TPEM)

[![Video Explanation](https://img.youtube.com/vi/u07eLf-s6TU/mqdefault.jpg)](https://youtu.be/u07eLf-s6TU)

[![Video Explanation](https://img.youtube.com/vi/61g5O0Jc-4I/mqdefault.jpg)](https://youtu.be/61g5O0Jc-4I)

### Complexity Analysis

- **Time Complexity:** O(n log n + k log n), where `n` is the number of projects. The complexity is dominated by the heap operations.
- **Space Complexity:** O(n), since we store all projects in the heaps.