# Leetcode - Maximum Amount of Gold

## Problem Description

In a gold mine `grid` of size `m x n`, each cell in this mine has an integer representing the amount of gold in that cell, with `0` if it is empty. Return the maximum amount of gold you can collect under the following conditions:

1. Every time you are located in a cell, you will collect all the gold in that cell.
2. From your position, you can walk one step to the left, right, up, or down.
3. You can't visit the same cell more than once.
4. Never visit a cell with `0` gold.
5. You can start and stop collecting gold from any position in the grid that has some gold.

**Constraints:**
- `m == grid.length`
- `n == grid[i].length`
- `1 <= m, n <= 15`
- `0 <= grid[i][j] <= 100`
- There are at most 25 cells containing gold.

## Solution

To solve this problem, we can use a depth-first search (DFS) approach to explore all possible paths in the grid. Here’s a step-by-step explanation:

We have a grid that looks like a map, and in each cell, there is a certain amount of gold. We want to collect the most gold possible by moving through the grid.



The `getMaximumGold` method takes a grid as input and returns the maximum amount of gold that can be collected. It uses a helper function `dfs` to perform a depth-first search from a given cell to explore all possible paths and collect gold.

1. **Initialize Variables:**
   - `max_gold` to keep track of the maximum gold collected.

2. **Define the DFS Function:**
   - The `dfs` function takes the current cell position `(i, j)` and the current amount of collected gold.
   - It marks the current cell as visited by setting its value to 0.
   - It explores all four possible directions (up, down, left, right) and recursively calls `dfs` if the next cell has gold.
   - It backtracks by resetting the current cell's value to its original amount after exploring all possible paths from the current cell.
   - It updates `max_gold` with the maximum amount of gold collected so far.

3. **Call DFS from Each Cell:**
   - Iterate through each cell in the grid.
   - If the cell has gold, call the `dfs` function from that cell.

4. **Return the Result:**
   - Return the value of `max_gold` which represents the maximum gold collected.



```python
class Solution(object):
    def getMaximumGold(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
```

## Usage

To use the solution, create an instance of the `Solution` class and call the `getMaximumGold` method with the input grid:

```python
solution = Solution()
grid = [
    [0,6,0],
    [5,8,7],
    [0,9,0]
]
result = solution.getMaximumGold(grid)
print(result)  # Output: 24
```

[Link to detailed explanation on AlgoMonster](https://algo.monster/liteproblems/1219)

[Link to detailed explanation on LinkedIn](https://www.linkedin.com/pulse/leetcode-1219-path-maximum-gold-aaron-j-mccullough-meg5e)

[Link to detailed explanation on Geeksforgeeks](https://www.geeksforgeeks.org/gold-mine-problem/)



## Check Out this videos

[![Video Explanation](https://img.youtube.com/vi/HlEdGHDYcrQ/mqdefault.jpg)](https://youtu.be/HlEdGHDYcrQ)

[![Video Explanation](https://img.youtube.com/vi/bst1LaMdHrw/mqdefault.jpg)](https://youtu.be/bst1LaMdHrw)

[![Video Explanation](https://img.youtube.com/vi/I1wllM_pozY/mqdefault.jpg)](https://youtu.be/I1wllM_pozY)



## Complexity Analysis

- **Time Complexity:** O(m * n * 4^(k)), where m and n are the dimensions of the grid, and k is the number of cells with gold. The DFS explores each cell and its four possible directions.
- **Space Complexity:** O(m * n), where m and n are the dimensions of the grid. The space complexity is due to the recursion stack used by DFS.