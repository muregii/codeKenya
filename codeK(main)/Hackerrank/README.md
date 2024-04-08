# Pascal's Triangle Generator

## Problem Description

Given an integer `n`, generate the first `n` rows of Pascal's triangle.

Pascal's triangle is a triangular array of integers where each number is the sum of the two numbers directly above it.

## Solution

The solution to this problem is implemented in the provided code snippet. Here's how it works:


We want to generate Pascal's triangle, which is a triangle of numbers where each number is the sum of the two numbers above it.

Here's how we can do it:
1. We start with an empty list to store the triangle.
2. Then, for each row from 1 to `n`, we create a new row and calculate each number by adding the numbers above and to the left and right.
3. We handle the edge cases where the number is the first or last in the row, where it's just '1'.
4. After generating each row, we add it to the triangle.
5. At the end, the triangle contains the first `n` rows of Pascal's triangle.

The key steps are:
- Initialize an empty list to store the triangle.
- For each row:
   - Create a new row.
   - Calculate each number by adding the numbers above and to the left and right.
   - Handle edge cases where the number is the first or last in the row.
   - Add the row to the triangle.
- Return the generated triangle.

Does this make sense? Great!

## Usage

To use the solution, you can call the `pascal_triangle` function with an integer representing the number of rows of Pascal's triangle you want to generate:

```python
n = 5
triangle = pascal_triangle(n)
print(triangle)
```

This will output:

```
[[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
```

## Complexity Analysis

- **Time Complexity:** O(n^2), where n is the number of rows of Pascal's triangle to generate. This is because we need to generate each number in each row of the triangle.
- **Space Complexity:** O(n^2), as we are storing the entire triangle in memory.