# Leetcode - Island Perimeter

## Problem Description

You are given a grid representing a map where `grid[i][j] = 1` represents land and `grid[i][j] = 0` represents water.

Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island. One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.


## Solution

To determine the perimeter of the island, we need to count the number of edges that form the boundary of the island. We can achieve this by traversing the grid and checking each land cell's surroundings.

Here's how we can approach this problem:

1. Iterate through each cell in the grid.
2. For each land cell (grid[i][j] == 1), check its four adjacent cells (up, down, left, right).
3. If any adjacent cell is water or outside the grid boundary, increment the perimeter by 1.
4. Repeat this process for all land cells in the grid.
5. At the end, the total perimeter represents the boundary of the island.

By counting the number of edges surrounding each land cell, we can determine the perimeter of the island.


Does this make sense? Great!"


## Usage

To use the solution, simply create an instance of the `Solution` class and call the `islandPerimeter` method with the input `grid` representing the grid map:

```python
solution = Solution()
# Define the grid representing the map
# grid = [[0,1,0,0],
#         [1,1,1,0],
#         [0,1,0,0],
#         [1,1,0,0]]
# Call the islandPerimeter method
result = solution.islandPerimeter(grid)
print(result)
```

```python
# grid = [[0,1,0,0],
#         [1,1,1,0],
#         [0,1,0,0],
#         [1,1,0,0]]
```


## Check Out this video


[![Video Explanation](https://img.youtube.com/vi/fISIuAFRM2s/mqdefault.jpg)](https://youtu.be/fISIuAFRM2s)


[![Video Explanation](https://img.youtube.com/vi/UcEYCLPWREQ/mqdefault.jpg)](https://youtu.be/UcEYCLPWREQ)






## Complexity Analysis

- **Time Complexity:** O(m*n), where m is the number of rows and n is the number of columns in the grid.
- **Space Complexity:** O(1), as we are using only a constant amount of extra space for storing the perimeter.

---