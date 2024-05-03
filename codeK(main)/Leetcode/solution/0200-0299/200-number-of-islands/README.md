# Leetcode - Number of Islands

## Problem Description

You are given an `m x n` 2D binary grid `grid` which represents a map of `1`s (land) and `0`s (water). Return the `number of islands`.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

## Solution

To solve this problem, we can use `Depth-First Search (DFS)` or `Breadth-First Search (BFS)` to `traverse the grid`. The idea is to `iterate through each cell in the grid`, and whenever we encounter a land cell `(grid[i][j] == '1')`, we perform a DFS or BFS to explore the entire island connected to that cell. While exploring the island, we mark visited cells as water to avoid revisiting them.

Here's how we can approach this problem:

1. Iterate through each cell in the grid.
2. If the current cell is land (grid[i][j] == '1') and has not been visited yet, perform a DFS or BFS to explore the entire island connected to that cell.
3. During the DFS or BFS traversal, mark visited cells as water (grid[i][j] = '0') to avoid revisiting them.
4. Increment the count of islands each time we encounter a new island (i.e., start a new DFS or BFS traversal).
5. Continue this process until we have visited all cells in the grid.

By counting the number of DFS or BFS traversals needed to cover all land cells, we can determine the number of islands in the grid.

## Usage

To use the solution, simply create an instance of the `Solution` class and call the `numIslands` method with the input `grid` representing the 2D binary grid:

```python
solution = Solution()
# Define the grid representing the map
# grid = [['1','1','0','0','0'],
#         ['1','1','0','0','0'],
#         ['0','0','1','0','0'],
#         ['0','0','0','1','1']]
# Call the numIslands method
result = solution.numIslands(grid)
print(result)
```

```python
# grid = [['1','1','0','0','0'],
#         ['1','1','0','0','0'],
#         ['0','0','1','0','0'],
#         ['0','0','0','1','1']]
```

[Link to detailed explanation on Medium](https://myinterview.guru/leetcode-200-number-of-islands-63b59ffa547f)


[Link to detailed explanation](https://omaryaya.com/leetcode-number-of-islands-leetcode-200)

## Check Out this video

[![Video Explanation](https://img.youtube.com/vi/__98uL6wst8/mqdefault.jpg)](https://youtu.be/__98uL6wst8)


[![Video Explanation](https://img.youtube.com/vi/sduu1n5uZUE/mqdefault.jpg)](https://youtu.be/sduu1n5uZUE)


[![Video Explanation](https://img.youtube.com/vi/pV2kpPD66nE/mqdefault.jpg)](https://youtu.be/pV2kpPD66nE)


## Complexity Analysis

- **Time Complexity:** O(m * n), where m is the number of rows and n is the number of columns in the grid. We visit each cell once during the DFS or BFS traversal.
- **Space Complexity:** O(m * n), where m is the number of rows and n is the number of columns in the grid. In the worst case, the space complexity can be O(m * n) for the call stack during DFS traversal or for the queue in BFS traversal.

---