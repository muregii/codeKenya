# Leetcode - Magic Squares In Grid

## Problem Description

A `3 x 3` **magic square** is a `3 x 3` grid filled with distinct numbers **from** 1 to 9 such that each row, column, and both diagonals all have the same sum.

Given a `row x col` `grid` of integers, determine how many `3 x 3` **magic square subgrids** are there?

**Note:** While a magic square can only contain numbers from `1` to `9`, the `grid` may contain numbers up to `15`.

**Constraints:**
- `row == grid.length`
- `col == grid[i].length`
- `1 <= row, col <= 10`
- `0 <= grid[i][j] <= 15`

## Solution

**Understanding the Problem:**
   - We need to find how many 3x3 subgrids in the given grid are magic squares.
   - A magic square is defined as a 3x3 grid where the sum of numbers in each row, column, and both diagonals is the same, and the numbers are distinct and range from 1 to 9.

**Breaking It Down**
   - **Magic Square Properties:**
     - For a grid to be a magic square, all numbers must be distinct and in the range from 1 to 9.
     - The sum of each row, column, and diagonal must be 15 (since 15 is the sum of any row, column, or diagonal in a 3x3 magic square filled with numbers 1 to 9).

   - **Iterating Over Subgrids:**
     - Since we're looking for 3x3 subgrids, iterate over each possible 3x3 subgrid within the larger grid.
     - For each subgrid, check whether it meets the conditions of a magic square.

**Implementation Approach:**
   - Traverse the grid to consider every possible 3x3 subgrid.
   - For each subgrid, check:
     - Whether it contains all numbers from 1 to 9 exactly once.
     - Whether the sum of the numbers in all rows, columns, and diagonals is 15.
   - Count how many such subgrids are valid magic squares.

**Algorithm Steps:**
   - **Check Each 3x3 Subgrid:** Iterate through the grid starting from each possible top-left corner of a 3x3 subgrid.
   - **Validate Magic Square:** For each 3x3 subgrid, ensure it contains the numbers 1 through 9 exactly once and that the sums of rows, columns, and diagonals are equal to 15.
   - **Count Valid Subgrids:** Increment the count if a subgrid is a magic square.
   - **Return the Result:** Return the total count of valid magic square subgrids.

### Python Code

```python
class Solution(object):
    def numMagicSquaresInside(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
```

### Example

```python
# Input
grid = [
  [4,3,8,4],
  [9,5,1,9],
  [2,7,6,2]
]

# Output
1
```

### Explanation
1. **Identifying Subgrids:** The grid has one possible 3x3 subgrid: `[[4,3,8],[9,5,1],[2,7,6]]`.
2. **Checking Magic Square:** This subgrid meets all the conditions of a magic square:
   - The numbers are distinct and within the range 1-9.
   - The sums of rows, columns, and diagonals are all equal to 15.
3. **Result:** The grid contains one 3x3 magic square.

### Usage

To use the solution, create an instance of the `Solution` class and call the `numMagicSquaresInside` method with the `grid` parameter:

```python
# Example usage
solution = Solution()
grid = [
  [4,3,8,4],
  [9,5,1,9],
  [2,7,6,2]
]
result = solution.numMagicSquaresInside(grid)
print(result)  # Output: 1
```

### Additional Resources

[Link to detailed explanation on Algo Monster](https://algo.monster/liteproblems/840)

[Link to detailed explanation on Geeksforgeeks](https://www.geeksforgeeks.org/count-magic-squares-in-a-grid/)

### Check Out These Video(s)

[![Video Explanation](https://img.youtube.com/vi/FV52wWrivNc/mqdefault.jpg)](https://youtu.be/FV52wWrivNc)

### Complexity Analysis

- **Time Complexity:** O((row-2) * (col-2) * 1), as each 3x3 subgrid is checked individually.
- **Space Complexity:** O(1), as only a few variables are used to keep track of the subgrid being checked.