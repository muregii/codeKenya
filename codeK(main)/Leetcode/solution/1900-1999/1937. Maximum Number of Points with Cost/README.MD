# Leetcode - Maximum Number of Points with Cost

## Problem Description

You are given an `m x n` integer matrix `points` **(0-indexed)**. Starting with `0` points, you want to **maximize** the number of points you can get from the matrix.

To gain points, you must pick one cell in **each row**. Picking the cell at coordinates `(r, c)` will **add** `points[r][c]` to your score.

However, you will lose points if you pick a cell too far from the cell that you picked in the previous row. For every two adjacent rows `r` and `r + 1` (where `0 <= r < m - 1`), picking cells at coordinates `(r, c1)` and `(r + 1, c2)` will **subtract** abs`(c1 - c2)` from your score.

Return *the **maximum** number of points you can achieve*.

`abs(x)` is defined as:
- `x` if `x >= 0`.
- `-x` if `x < 0`.

### Constraints:
- `m == points.length`
- `n == points[r].length`
- `1 <= m, n <= 10^5`
- `1 <= m * n <= 10^5`
- `0 <= points[r][c] <= 10^5`

## Solution

**Understanding the Problem:**
   - The objective is to maximize the total points obtained from picking one cell per row in the matrix.
   - While picking cells, there's a penalty in points if the column chosen in row `r + 1` differs from the column chosen in row `r`.
   - Therefore, the task is to consider both the points gained from cells and the penalties incurred from choosing cells that are too far apart in adjacent rows.

**Breaking It Down**
   - **Maximizing Points:**
     - For each row, you must consider picking cells in a way that maximizes the overall points.
   - **Penalty Handling:**
     - The penalty for selecting a cell in row `r + 1` at a column different from the one in row `r` is the absolute difference in column indices (`abs(c1 - c2)`).

**Implementation Approach:**
   - Start by processing each row and consider all possible cells in the next row.
   - Use dynamic programming to calculate the maximum points achievable for each cell, adjusting for the penalty between adjacent rows.
   - The key is to propagate the best achievable score from one row to the next by minimizing the penalty for column changes.

**Algorithm Steps:**
   - **Row Processing:** For each row, calculate the best possible points by adding the value of the cell to the maximum points from the previous row, adjusting for the penalty.
   - **Optimization with Dynamic Programming:** Keep track of the maximum points at each column and propagate them to the next row.
   - **Final Result:** The maximum points after processing all rows will be the answer.

### Python Code

```python
class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        
```

### Example

```python
# Input
points = [[1, 2, 3], [1, 5, 1], [3, 1, 1]]

# Output
9
```

### Explanation:
1. In the first row, the possible points are `[1, 2, 3]`.
2. In the second row, the optimal choices are to pick column 1 (`points[1][1] = 5`), adjusting for penalties.
3. In the final row, picking column 0 yields the maximum points.
4. The final result is `9` points.

### Usage

To use the solution, create an instance of the `Solution` class and call the `maxPoints` method with the `points` matrix:

```python
# Example usage
solution = Solution()
points = [[1, 2, 3], [1, 5, 1], [3, 1, 1]]
result = solution.maxPoints(points)
print(result)  # Output: 9
```

### Additional Resources

[Link to detailed explanation on Algo Monster](https://algo.monster/liteproblems/1937)


### Check Out These Video(s)

[![Video Explanation](https://img.youtube.com/vi/STEJHYc9rMw/mqdefault.jpg)](https://youtu.be/STEJHYc9rMw)

[![Video Explanation](https://img.youtube.com/vi/lk7WUhAwYGA/mqdefault.jpg)](https://youtu.be/lk7WUhAwYGA)

[![Video Explanation](https://img.youtube.com/vi/ik1y7fz8AOc/mqdefault.jpg)](https://youtu.be/ik1y7fz8AOc)

### Complexity Analysis

- **Time Complexity:** O(m * n), where `m` is the number of rows and `n` is the number of columns in the matrix. Each cell is processed once per row.
- **Space Complexity:** O(n), as we only maintain the points for the current row and the next row during the calculation.