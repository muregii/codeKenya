# Leetcode - Build a Matrix With Conditions

## Problem Description

You are given a positive integer `k`. Additionally, you have:

- A 2D integer array `rowConditions` of size `n` where `rowConditions[i] = [above_i, below_i]`, and
- A 2D integer array `colConditions` of size `m` where `colConditions[i] = [left_i, right_i]`.

The two arrays contain integers from `1` to `k`.

You need to build a `k x k` matrix that contains each of the numbers from `1` to `k` **exactly once**,  the remaining cells filled with `0`. 

The matrix must satisfy the following conditions:

- The number `above-i` should appear in a row that is strictly above the row at which the number `below-i` appears for all `i` from `0` to `n - 1`.

- The number `left-i` should appear in a **column** that is strictly **left** of the column at which the number `right-i` appears for all `i` from `0` to` m - 1`.

Return ***any** matrix that satisfies the conditions*. If no solution exists, return an empty matrix.

**Constraints:**
- `2 <= k <= 400`
- `1 <= rowConditions.length, colConditions.length <= 10^4`
- `rowConditions[i].length == colConditions[i].length == 2`
- `1 <= above_i, below_i, left_i, right_i <= k`
- `above_i != below_i`
- `left_i != right_i`

## Solution

To solve this problem, create a matrix that meets both the row and column conditions. Break down the problem into two parts: determining the order of elements in the rows based on `rowConditions` and determining the order in the columns based on `colConditions`.

1. **Understanding the Problem:**
   - We have a set of constraints that dictate the relative positions of numbers in the matrix, both by rows and by columns.
   - Our goal is to arrange the numbers from `1` to `k` in a matrix so that all conditions are satisfied.

2. **Simulating the Process:**
   - **Step 1: Determine Row Order**
     - Treat the row conditions as a directed graph where each pair `[above_i, below_i]` represents an edge from `above_i` to `below_i`.
     - Perform a topological sort on this graph to determine the correct order of numbers in the rows.
   
   - **Step 2: Determine Column Order**
     - Similarly, treat the column conditions as a directed graph where each pair `[left_i, right_i]` represents an edge from `left_i` to `right_i`.
     - Perform a topological sort on this graph to determine the correct order of numbers in the columns.

   - **Step 3: Construct the Matrix**
     - Using the row and column orders obtained from the topological sorts, place each number from `1` to `k` in the matrix at the appropriate position.
     - If at any point the topological sort is not possible (indicating a cycle in the graph), return an empty matrix.

3. **Algorithm Steps:**
   - Build the directed graphs for row and column conditions.
   - Perform topological sorts to determine the valid order of rows and columns.
   - Populate the matrix based on these orders, ensuring each number appears exactly once.

### Example

Suppose you have:
- `k = 3`
- `rowConditions = [[1, 2], [2, 3]]`
- `colConditions = [[1, 3], [2, 3]]`

1. **Determine Row Order:**
   - The row order based on `rowConditions` is `[1, 2, 3]`.
   
2. **Determine Column Order:**
   - The column order based on `colConditions` is `[1, 2, 3]`.

3. **Construct the Matrix:**

The resulting matrix is:

```python
[
  [1, 0, 0],
  [0, 2, 0],
  [0, 0, 3]
]
```

### Python Code

```python
class Solution(object):
    def buildMatrix(self, k, rowConditions, colConditions):
        """
        :type k: int
        :type rowConditions: List[List[int]]
        :type colConditions: List[List[int]]
        :rtype: List[List[int]]
        """
        
```

### Usage

To use the solution, create an instance of the `Solution` class and call the `buildMatrix` method with the `k`, `rowConditions`, and `colConditions` arrays:

```python
# Example usage
solution = Solution()
k = 3
rowConditions = [[1, 2], [2, 3]]
colConditions = [[1, 3], [2, 3]]
matrix = solution.buildMatrix(k, rowConditions, colConditions)
print(matrix)  # Output: [[1, 0, 0], [0, 2, 0], [0, 0, 3]]
```

### Complexity Analysis

- **Time Complexity:** O(k + n + m), where `k` is the size of the matrix, and `n` and `m` are the sizes of the `rowConditions` and `colConditions` arrays, respectively.
- **Space Complexity:** O(k), for storing the graph, in-degree arrays, and the result matrix.
