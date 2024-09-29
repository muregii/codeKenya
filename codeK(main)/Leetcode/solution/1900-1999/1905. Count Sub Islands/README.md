# Leetcode - Count Sub-Islands

## Problem Description

You are given two `m x n` binary matrices `grid1` and `grid2` containing only `0`'s (representing water) and` 1`'s (representing land). An **island** is a group of 1's connected **4-directionally** (horizontal or vertical). Any cells outside of the grid are considered water cells.

An island in `grid2` is considered a **sub-island** if there is an island in `grid1` that contains **all** the cells that make up this island in `grid2`.

Return the number of islands in `grid2` that are considered sub-islands.

### Constraints:

- `m == grid1.length == grid2.length`
- `n == grid1[i].length == grid2[i].length`
- `1 <= m, n <= 500`
- `grid1[i][j]` and `grid2[i][j]` are either 0 or 1.

## Solution

### Understanding the Problem:

The task is to count how many islands in `grid2` are completely contained within islands in `grid1`. An island in `grid2` is considered a sub-island if every `1` in that island also exists as a `1` in the corresponding position in `grid1`.

### Breaking It Down:

1. **What is an Island?**:

   - An island is a group of `1`'s connected 4-directionally (up, down, left, right).
   - We can find islands using a flood fill or depth-first search (DFS) technique.

2. **Sub-Islands**:

   - An island in `grid2` is a sub-island if it is fully contained within an island in `grid1`. This means every land cell (1) in `grid2`'s island must also be land in `grid1` at the same coordinates.

3. **Approach**:
   - Use DFS to explore each island in `grid2`.
   - During the DFS, ensure that for every land cell (1) in `grid2`, the corresponding cell in `grid1` is also land. If we find any mismatch (a cell in `grid2` is land but the corresponding cell in `grid1` is water), this island is not a sub-island.

### Algorithm Steps:

1. **DFS Helper Function**:

   - Create a DFS function that checks if an island in `grid2` is a sub-island. It will explore all `1`'s in `grid2` and ensure the corresponding cells in `grid1` are also `1`.

2. **Main Logic**:

   - Loop through every cell in `grid2`. When a `1` is found (indicating the start of an island), perform a DFS to check if it's a sub-island.
   - If it is a sub-island, increment the count.

3. **Return Result**:
   - Return the total count of sub-islands found in `grid2`.

### Python Code

```python
class Solution(object):
    def countSubIslands(self, grid1, grid2):
        """
        :type grid1: List[List[int]]
        :type grid2: List[List[int]]
        :rtype: int
        """

```

### Example

```python
# Input:
grid1 = [
    [1, 1, 1, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 1, 1],
    [1, 0, 0, 0, 0],
    [1, 1, 0, 1, 1]
]

grid2 = [
    [1, 1, 1, 0, 0],
    [0, 0, 1, 1, 0],
    [0, 1, 0, 1, 1],
    [1, 0, 1, 0, 0],
    [1, 1, 0, 1, 1]
]

# Output:
result = solution.countSubIslands(grid1, grid2)
print(result)  # Output: 3
```

### Explanation:

1. We perform DFS on all islands in `grid2` and compare them with the corresponding cells in `grid1`.
2. There are 3 sub-islands in `grid2` that match completely with islands in `grid1`, so the result is 3.

### Usage

To use the solution, create an instance of the `Solution` class and call the `countSubIslands` method with `grid1` and `grid2` as the input.

```python
solution = Solution()
grid1 = [
    [1, 1, 1, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 1, 1],
    [1, 0, 0, 0, 0],
    [1, 1, 0, 1, 1]
]
grid2 = [
    [1, 1, 1, 0, 0],
    [0, 0, 1, 1, 0],
    [0, 1, 0, 1, 1],
    [1, 0, 1, 0, 0],
    [1, 1, 0, 1, 1]
]
result = solution.countSubIslands(grid1, grid2)
print(result)  # Output: 3
```

### Additional Resources

-
- [Link to detailed explanation on Algo Monster ](https://algo.monster/liteproblems/1905)

## Check Out this video

[![Video Explanation](https://img.youtube.com/vi/o1rVOYwcRd0/mqdefault.jpg)](https://youtu.be/o1rVOYwcRd0)

[![Video Explanation](https://img.youtube.com/vi/mLpW3qfbNJ8/mqdefault.jpg)](https://youtu.be/mLpW3qfbNJ8)

### Complexity Analysis

- **Time Complexity:** O(m \* n), where `m` is the number of rows and `n` is the number of columns in the grid. Each cell is visited at most once.
- **Space Complexity:** O(m \* n), which is the maximum depth of the recursion stack used during the DFS traversal.
