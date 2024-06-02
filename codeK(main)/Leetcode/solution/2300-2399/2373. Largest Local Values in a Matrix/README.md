# Leetcode - Largest Local Values in a Matrix

## Problem Description

You are given an `n x n` integer matrix `grid`.

Generate an integer matrix `maxLocal` of size `(n - 2) x (n - 2)` such that:

`maxLocal[i][j]` is equal to the **largest** value of the `3 x 3` matrix in `grid` centered around row `i + 1` and column `j + 1`.

In other words, we want to find the largest value in every contiguous `3 x 3` matrix in `grid`.

*Return the generated matrix*.

**Constraints:**

- `n == grid.length == grid[i].length`
- `3 <= n <= 100`
- `1 <= grid[i][j] <= 100`

## Solution

To solve this problem, we need to iterate through each possible `3 x 3` submatrix in the given `n x n` matrix `grid` and find the maximum value in each submatrix. Here's a step-by-step approach to achieve this:

1. **Initialize the Result Matrix**: Create an empty matrix `maxLocal` of size `(n - 2) x (n - 2)` to store the results.
2. **Iterate Through the Grid**: Loop through each possible `3 x 3` submatrix in the grid. This requires nested loops where the outer loops run from `0` to `n - 3`.
3. **Find the Maximum Value**: For each `3 x 3` submatrix, find the maximum value by iterating through its elements.
4. **Store the Maximum Value**: Store the found maximum value in the corresponding position in the `maxLocal` matrix.
5. **Return the Result Matrix**: After processing all submatrices, return the `maxLocal` matrix.

This method ensures that we correctly find and store the maximum values for each `3 x 3` submatrix in the given grid.

## Usage

To use the solution, create an instance of the `Solution` class and call the `largestLocal` method with the input parameter `grid`:

```python
class Solution(object):
    def largestLocal(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[List[int]]
        """

# Example Usage
solution = Solution()
grid = [
    [9, 9, 8, 1],
    [5, 6, 2, 6],
    [8, 2, 6, 4],
    [6, 2, 2, 2]
]
result = solution.largestLocal(grid)
print(result)  # Output: [[9, 9], [8, 6]]
```

## Explanation

1. **Input**: The matrix `grid` is given.
2. **Initialize Result Matrix**: Create the `maxLocal` matrix of size `(n - 2) x (n - 2)`.
3. **Iterate Through Grid**: Loop through each position in the `grid` where a `3 x 3` submatrix can fit.
4. **Find Maximum Value**: For each `3 x 3` submatrix, find the maximum value by checking all its elements.
5. **Store Maximum Value**: Store the maximum value in the corresponding cell of the `maxLocal` matrix.
6. **Return Result**: Return the `maxLocal` matrix after processing all possible `3 x 3` submatrices.

[Link to detailed explanation on GeeksforGeeks](https://www.geeksforgeeks.org/minimum-cells-required-reach-destination-jumps-equal-cell-values/)


[Link to detailed explanation on GeeksforGeeks](https://www.geeksforgeeks.org/program-to-find-the-maximum-element-in-a-matrix/)


[Link to detailed explanation on GeeksforGeeks](https://www.geeksforgeeks.org/coordinates-of-the-last-cell-in-a-matrix-on-which-performing-given-operations-exits-from-the-matrix/)


[Link to detailed explanation on Medium](https://medium.com/deuk/algorithms-and-data-structures-in-python-beginner-array-problem-largest-local-values-in-a-matrix-eb49637ebe35)




## Check Out these videos

[![Video Explanation](https://img.youtube.com/vi/vP5FAH910B0/mqdefault.jpg)](https://youtu.be/vP5FAH910B0)

[![Video Explanation](https://img.youtube.com/vi/wdTRu9sarFA/mqdefault.jpg)](https://youtu.be/wdTRu9sarFA)

## Complexity Analysis

- **Time Complexity:** O(n^2), where n is the size of the input grid. We iterate through each possible `3 x 3` submatrix in the `n x n` grid.
- **Space Complexity:** O((n-2)^2), where (n-2)^2 is the size of the `maxLocal` result matrix. This space is used to store the results.