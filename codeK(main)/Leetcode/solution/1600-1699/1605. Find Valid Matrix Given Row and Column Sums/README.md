# Leetcode - Restore Matrix

## Problem Description

You are given two arrays `rowSum` and `colSum` of non-negative integers where `rowSum[i]` is the sum of the elements in the `i`-th row and `colSum[j]` is the sum of the elements of the `j`-th column of a 2D matrix. In other words, you do not know the elements of the matrix, but you do know the sums of each row and column.

Find any matrix of **non-negative** integers of size `rowSum.length x colSum.length` that satisfies the `rowSum` and `colSum` requirements.

Return *a 2D array representing any matrix that fulfills the requirements*. It is guaranteed that **at least one ** matrix that fulfills the requirements exists.

**Constraints:**
- `1 <= rowSum.length, colSum.length <= 500`
- `0 <= rowSum[i], colSum[i] <= 10^8`
- `sum(rowSum) == sum(colSum)`

## Solution

To solve this problem, construct a matrix that matches the given row and column sums. The key is to iteratively allocate values to each cell in a greedy manner.

1. **Understanding the Problem:**
   - We are given two arrays: `rowSum` and `colSum`. Each element in `rowSum` represents the sum of elements in a specific row, and each element in `colSum` represents the sum of elements in a specific column.
   - Our task is to fill in the values in the matrix such that these row and column sums are satisfied.

2. **Simulating the Process:**
   - Start by initializing an empty matrix with the dimensions corresponding to the lengths of `rowSum` and `colSum`.
   - For each cell in the matrix, we assign the minimum of the current row sum and column sum. This ensures that we do not exceed the required sum for either the row or the column.
   - After assigning this value, we subtract it from both the current row sum and column sum, effectively "reducing" the remaining sums that need to be distributed.
   - Continue this process until all cells are filled and all row and column sums are satisfied.

3. **Algorithm Steps:**
   - Initialize an empty matrix of size `rowSum.length x colSum.length`.
   - Iterate over each cell `(i, j)` in the matrix:
     - Assign the value `min(rowSum[i], colSum[j])` to the cell.
     - Subtract this value from both `rowSum[i]` and `colSum[j]`.
     - Move to the next cell and repeat the process.
   - The resulting matrix will satisfy the given row and column sums.

### Example

Suppose you have:
- `rowSum = [3, 8]`
- `colSum = [4, 7]`

1. Process the matrix:
   - Start with an empty matrix of size `2x2`.
   - Assign `min(3, 4) = 3` to the first cell `(0, 0)`. Now, `rowSum = [0, 8]` and `colSum = [1, 7]`.
   - Assign `min(0, 7) = 0` to the next cell `(0, 1)`. `rowSum = [0, 8]` and `colSum = [1, 7]`.
   - Assign `min(8, 1) = 1` to the cell `(1, 0)`. Now, `rowSum = [0, 7]` and `colSum = [0, 7]`.
   - Finally, assign `min(7, 7) = 7` to the last cell `(1, 1)`. `rowSum = [0, 0]` and `colSum = [0, 0]`.

2. The result is:

```python
[
  [3, 0],
  [1, 7]
]
```

### Python Code

```python
class Solution(object):
    def restoreMatrix(self, rowSum, colSum):
        """
        :type rowSum: List[int]
        :type colSum: List[int]
        :rtype: List[List[int]]
        """
        
```

### Usage

To use the solution, create an instance of the `Solution` class and call the `restoreMatrix` method with the `rowSum` and `colSum` arrays:

```python
# Example usage
solution = Solution()
rowSum = [3, 8]
colSum = [4, 7]
matrix = solution.restoreMatrix(rowSum, colSum)
print(matrix)  # Output: [[3, 0], [1, 7]]
```

### Additional Resources

[Link to detailed explanation on Algo Monster](https://algo.monster/liteproblems/1605)

### Check Out These Videos

[![Video Explanation](https://img.youtube.com/vi/Ks6fGnXkHPg/mqdefault.jpg)](https://youtu.be/Ks6fGnXkHPg)

[![Video Explanation](https://img.youtube.com/vi/jWTcK-BaLEk/mqdefault.jpg)](https://youtu.be/jWTcK-BaLEk)

### Complexity Analysis

- **Time Complexity:** O(m * n), where `m` is the number of rows and `n` is the number of columns in the matrix. Each cell in the matrix is filled once.
- **Space Complexity:** O(m * n), for storing the resulting matrix.