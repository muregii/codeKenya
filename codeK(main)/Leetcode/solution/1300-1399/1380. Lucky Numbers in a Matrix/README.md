# Leetcode - Lucky Numbers in a Matrix

## Problem Description

Given an `m x n` matrix of **distinct** numbers, return *all **lucky numbers** in the matrix in **any** order*.

A **lucky number** is an element of the matrix such that it is the minimum element in its row and the maximum in its column.

**Constraints:**
- `m == mat.length`
- `n == mat[i].length`
- `1 <= n, m <= 50`
- `1 <= matrix[i][j] <= 10^5`
- All elements in the matrix are distinct.

## Solution

To solve this problem, identify numbers in the matrix that are both the minimum in their row and the maximum in their column.

1. **Understanding the Problem:**
   - You have a matrix (a grid of numbers), and every number in this matrix is unique.
   - A "lucky number" is a number that is the smallest in its row but the largest in its column.
   - Your task is to find all such "lucky numbers" in the matrix.

2. **Simulating the Process:**
   - First, for each row in the matrix, find the smallest number.
   - Then, for each of those smallest numbers, check if it is also the largest number in its column.
   - If it is, then that number is a lucky number, and we add it to our result.

3. **Algorithm Steps:**
   - Create a list to store the result of lucky numbers.
   - For each row in the matrix:
     - Find the minimum value in that row.
     - Identify the column index of this minimum value.
     - Check if this minimum value is the maximum value in its corresponding column.
     - If it is, add it to the list of lucky numbers.
   - Return the list of lucky numbers.

### Example

Suppose you have:
- A matrix:

```python
  3  7  8
  9 11 13
  15 16 17

  1. Process the matrix:
     - Row 1: Minimum is `3` (column index 0), maximum in column 0 is `15`, so not a lucky number.
     - Row 2: Minimum is `9` (column index 0), maximum in column 0 is `15`, so not a lucky number.
     - Row 3: Minimum is `15` (column index 0), and it is also the maximum in column 0, so `15` is a lucky number.

  2. The result is `[15]`.
```


### Python Code

```python
class Solution(object):
    def luckyNumbers(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """

```

### Usage

To use the solution, create an instance of the `Solution` class and call the `luckyNumbers` method with the `matrix`:

```python
# Example usage
solution = Solution()
matrix = [
    [3, 7, 8],
    [9, 11, 13],
    [15, 16, 17]
]
lucky_numbers = solution.luckyNumbers(matrix)
print(lucky_numbers)  # Output: [15]
```

### Additional Resources

[Link to detailed explanation on Algo Monster]((https://algo.monster/liteproblems/1380))

### Check Out These Videos

[![Video Explanation](https://img.youtube.com/vi/ceuQgACqr78/mqdefault.jpg)](https://youtu.be/ceuQgACqr78)

[![Video Explanation](https://img.youtube.com/vi/GIdJO7L6uq8/mqdefault.jpg)](https://youtu.be/GIdJO7L6uq8)

### Complexity Analysis

- **Time Complexity:** O(m * n), where `m` is the number of rows and `n` is the number of columns in the matrix. We must check every row and column.
- **Space Complexity:** O(1), since we only use a fixed amount of space to store the result and intermediate variables.