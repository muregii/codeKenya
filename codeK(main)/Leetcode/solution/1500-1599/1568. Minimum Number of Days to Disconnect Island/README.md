# Leetcode - Minimum Number of Days to Disconnect Island

## Problem Description

You are given an `m x n` binary `grid` where `1` represents land and `0` represents water. An **island** is defined as a maximal **4-directionally** (horizontal or vertical) connected group of `1`s.

The grid is said to be **connected** if we have  **exactly one island** otherwise is said **disconnected**.

In one day, you are allowed to change **any** single land cell (`1`) into a water cell (`0`).

Return *the minimum number of days required to disconnect the grid*.

**Constraints:**
- `m == grid.length`
- `n == grid[i].length`
- `1 <= m, n <= 30`
- `grid[i][j]` is either `0` or `1`.

## Solution

**Understanding the Problem:**
   - The goal is to find the minimum number of days needed to disconnect the grid such that it no longer forms a single connected island.
   - The problem revolves around transforming a connected island into either multiple disconnected islands or no islands at all by converting land cells (`1`) into water cells (`0`).

**Breaking It Down**
   - **Initial Check for Disconnected Grid:**
     - If the grid is already disconnected, the result is `0` because no changes are needed.
     
   - **Critical Points for Disconnection:**
     - The key observation is to identify critical points on the grid where removing a single cell will disconnect the grid.
     - After removing a cell, we check if the grid becomes disconnected by performing a DFS or BFS to see if there is still one connected island.

   - **DFS/BFS for Connectivity Check:**
     - Use DFS or BFS to explore the grid and count the number of connected components. If there's more than one, the grid is disconnected.
     - If the grid remains connected after removing one land cell, try removing two cells.

**Implementation Approach:**
   - **Check Initial Connectivity:** Perform a DFS/BFS to determine if the grid is initially connected.
   - **Single Cell Removal:** Iterate through each land cell, temporarily remove it, and check if this results in a disconnected grid.
   - **Two Cell Removal:** If removing one cell doesn't work, try removing any two different cells and check if that leads to disconnection.

**Algorithm Steps:**
   - **Initial Check:** Perform a DFS/BFS to determine if the grid is initially connected.
   - **Remove One Cell:** For each land cell, remove it and check if the grid becomes disconnected. If yes, return `1`.
   - **Remove Two Cells:** If removing one cell isn't enough, try removing pairs of cells and check for disconnection. If successful, return `2`.
   - **Return Result:** If none of the above steps work, return `2` since the grid can be disconnected by removing two cells.

### Python Code

```python
class Solution(object):
    def minDays(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
```

### Example

```python
# Input
grid = [
  [1,1],
  [1,0]
]

# Output
2
```

### Explanation
1. **Initial Connectivity Check:** The grid is initially connected.
2. **One Cell Removal:** Removing any one of the land cells does not disconnect the grid.
3. **Two Cell Removal:** Removing two cells (e.g., `grid[0][0]` and `grid[1][0]`) will disconnect the grid, making the result `2`.

### Usage

To use the solution, create an instance of the `Solution` class and call the `minDays` method with the `grid` parameter:

```python
# Example usage
solution = Solution()
grid = [
  [1,1],
  [1,0]
]
result = solution.minDays(grid)
print(result)  # Output: 2
```

### Additional Resources

[Link to detailed explanation on Algo Monster](https://algo.monster/liteproblems/1568)

### Check Out These Video(s)

[![Video Explanation](https://img.youtube.com/vi/aO-QbJ5eZwU/mqdefault.jpg)](https://youtu.be/aO-QbJ5eZwU)

[![Video Explanation](https://img.youtube.com/vi/Cta6Sa9EMYw/mqdefault.jpg)](https://youtu.be/Cta6Sa9EMYw)

### Complexity Analysis

- **Time Complexity:** O((m * n)^2), where `m` and `n` are the dimensions of the grid. This accounts for checking each cell and each possible removal.
- **Space Complexity:** O(m * n), for the DFS/BFS stack or queue used to explore the grid.