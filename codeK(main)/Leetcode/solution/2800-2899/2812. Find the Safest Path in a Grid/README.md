# Leetcode - Maximum Safeness Factor of a Path

## Problem Description

You are given a **0-indexed** 2D matrix grid of size `n x n`, where `(r, c)` represents:

- A cell containing a thief if `grid[r][c] = 1`
- An empty cell if `grid[r][c] = 0`

You are initially positioned at cell `(0, 0)`. In one move, you can move to any adjacent cell in the grid, including cells containing thieves.

The **safeness factor** of a path on the grid is defined as the **minimum** Manhattan distance from any cell in the path to any thief in the grid.

Return *the **maximum safeness** factor of all paths leading to cell* `(n - 1, n - 1)`.

An **adjacent** cell of cell `(r, c)`, is one of the cells `(r, c + 1)`, `(r, c - 1)`, `(r + 1, c)` and `(r - 1, c)` if it exists.

The **Manhattan distance** between two cells `(a, b)` and `(x, y)` is equal to `|a - x| + |b - y|`, where `|val|` denotes the absolute value of `val`.

**Constraints:**
- `1 <= grid.length == n <= 400`
- `grid[i].length == n`
- `grid[i][j]` is either `0` or `1`.
- There is at least one thief in the grid.

## Solution

We can use a breadth-first search (BFS) approach to determine the safeness factor.

We have a grid that looks like a chessboard. Some squares have thieves, and some squares are empty. We want to move from the top-left corner to the bottom-right corner of the grid. But, we want to do this in a way that keeps us as far away from the thieves as possible.

Here's how we can do it:

1. We start at the top-left corner and look at all the neighboring squares we can move to.
2. For each square, we figure out how far it is from the nearest thief using a distance measure called Manhattan distance.
3. We keep track of the smallest distance to a thief for each path we consider.
4. We choose the path that has the largest of these smallest distances, meaning we are as far away from the thieves as possible at our closest point.


The `maximumSafenessFactor` method takes a grid as input and returns the maximum safeness factor for a path from the top-left to the bottom-right corner of the grid. It uses a BFS approach to explore all possible paths and calculate the safeness factor.

1. **Initialize Variables:**
   - A queue for BFS.
   - A matrix to store the minimum distance to any thief for each cell.
   - A variable to keep track of the maximum safeness factor.

2. **Precompute Distances to Thieves:**
   - Use BFS to calculate the minimum Manhattan distance from each cell to the nearest thief.
   - Store these distances in a matrix.

3. **BFS to Find Maximum Safeness Factor:**
   - Start BFS from the top-left corner.
   - For each cell, calculate the safeness factor (minimum distance to any thief along the path).
   - Update the maximum safeness factor if a higher value is found.
   - Move to adjacent cells and continue BFS.

4. **Return the Result:**
   - Return the maximum safeness factor found.


```python

class Solution(object):
    def maximumSafenessFactor(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
```

## Usage

To use the solution, create an instance of the `Solution` class and call the `maximumSafenessFactor` method with the input grid:

```python
solution = Solution()
grid = [
    [0, 0, 0],
    [0, 1, 0],
    [0, 0, 0]
]
result = solution.maximumSafenessFactor(grid)
print(result)  # Output: 2
```


[Link to detailed explanation on AlgoMonster](https://algo.monster/liteproblems/2812)

[Link to detailed explanation on Medium](https://medium.com/@leetcodein5mins/leet-code-solution-weekly-contest-2812-find-the-safest-path-in-a-grid-44a0632f9ef3)

[Link to detailed explanation on Geeksforgeeks](https://www.geeksforgeeks.org/find-shortest-safe-route-in-a-path-with-landmines/)




## Check Out this videos

[![Video Explanation](https://img.youtube.com/vi/-5mQcNiVWTs/mqdefault.jpg)](https://youtu.be/-5mQcNiVWTs)

[![Video Explanation](https://img.youtube.com/vi/vsM-uGbLDyU/mqdefault.jpg)](https://youtu.be/vsM-uGbLDyU)

[![Video Explanation](https://img.youtube.com/vi/ZqEX8Eab3ZA/mqdefault.jpg)](https://youtu.be/ZqEX8Eab3ZA)

## Complexity Analysis

- **Time Complexity:** O(n^2), where n is the dimension of the grid. We perform BFS twice, first to compute distances to thieves and second to find the maximum safeness factor.
- **Space Complexity:** O(n^2), where n is the dimension of the grid. We use additional space to store distances and for the BFS queue.