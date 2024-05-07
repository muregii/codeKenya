# Leetcode - Minimum Falling Path Sum II

## Problem Description

Given an `n x n` integer matrix `grid`, return the minimum sum of a falling path with non-zero shifts.

`A falling path with non-zero shifts` is a choice of exactly one element from each row of `grid` such that no two elements chosen in adjacent rows are in the same column.

## Solution

To solve this problem, we can use dynamic programming. We'll define a function `dp` to represent the minimum sum of a falling path with non-zero shifts ending at position `(i, j)` in the input matrix `grid`.

Here's how we can approach this problem:

1. Initialize a 2D array `dp` of size `(n, n)`, where `n` is the number of rows in the input matrix `grid`.
2. Initialize the first row of `dp` with the values from the first row of `grid`.
3. For each subsequent row `i` (starting from the second row), calculate the minimum sum of a falling path with non-zero shifts ending at position `(i, j)` for each column `j`.
4. The minimum sum for position `(i, j)` can be obtained by adding the value of `grid[i][j]` to the minimum of the values in the previous row `i - 1` at positions `(i - 1, j)`, `(i - 1, j - 1)`, and `(i - 1, j + 1)`, with the condition that these positions are valid.
5. Update the value of `dp[i][j]` with the minimum sum calculated in step 4.
6. After processing all rows, the minimum sum of a falling path with non-zero shifts is the minimum value in the last row of the `dp` array.

By dynamically calculating the minimum sum of falling paths with non-zero shifts for each position in the input matrix `grid`, we can determine the overall minimum sum.

## Usage

To use the solution, create an instance of the `Solution` class and call the `minFallingPathSum` method with the input parameter `grid`:

```python
solution = Solution()
# Define the input matrix grid
# grid = [[2,1,3],[6,5,4],[7,8,9]]
# Call the minFallingPathSum method
result = solution.minFallingPathSum(grid)
print(result)
```

```python
# grid = [[2,1,3],[6,5,4],[7,8,9]]
```

[Link to detailed explanation on AlgoMonster](https://algo.monster/liteproblems/path-sum-ii)

[Link to detailed explanation](https://fastercapital.com/content/Dynamic-programming--Demystifying-Dynamic-Programming-with-IOI-Techniques.html)

[Link to detailed explanation on Geeksforgeeks](https://www.geeksforgeeks.org/introduction-to-dynamic-programming-data-structures-and-algorithm-tutorials/)

[Link to detailed explanation](https://takeuforward.org/data-structure/minimum-maximum-falling-path-sum-dp-12/)


## Check Out this video

[![Video Explanation](https://img.youtube.com/vi/LCC0gTGEK1Y/mqdefault.jpg)](https://youtu.be/LCC0gTGEK1Y)

[![Video Explanation](https://img.youtube.com/vi/_b8sptrsFEM/mqdefault.jpg)](https://youtu.be/_b8sptrsFEM)

## Complexity Analysis

- **Time Complexity:** O(n^2), where n is the number of rows in the input matrix `grid`. We iterate through each cell in the grid and calculate the minimum sum for each cell based on the previous row.
- **Space Complexity:** O(n^2), where n is the number of rows in the input matrix `grid`. We use additional space for the 2D array `dp` to store intermediate results.