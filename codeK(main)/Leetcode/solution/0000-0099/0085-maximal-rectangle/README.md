# Leetcode - Maximal Rectangle

## Problem Description

Given a `rows x cols` binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.


## Solution

To find the largest rectangle in a binary matrix filled with 0's and 1's, we have a grid where some cells are filled with water (1's) and some are not (0's). Now, we need to find the largest rectangle containing only water cells (1's).

We need to clarify how to systematically search for rectangles containing only 1's and determine their areas.

Here's how:

- Calculate the height of bars for each row of the matrix.
- Apply the "Largest Rectangle in Histogram" approach to find the largest rectangle in each row.
- Track the maximum area across all rows to find the largest rectangle in the binary matrix.

For example, if the elevation map is [0,1,0,2,1,0,1,3,2,1,2,1], the total amount of trapped water is 6 units.

Does this make sense? Great!"

## Usage

To use the solution, implement the `maximalRectangle` method within the `Solution` class. This method takes a binary matrix `matrix` as input, where each element represents a cell in the matrix filled with either 0 or 1. The method returns an integer representing the area of the largest rectangle containing only 1's in the binary matrix.

You can instantiate the `Solution` class and call the `maximalRectangle` method with the binary matrix as shown below:

```python
solution = Solution()
matrix = [
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]
result = solution.maximalRectangle(matrix)
print(result)  # Output: 6
```

Ensure that the `matrix` variable is a list of lists where each inner list represents a row of the binary matrix, and each element of the inner list is a string representing either '0' or '1'.


[Link to detailed explanation on Medium](https://rohithv63.medium.com/85-maximal-rectangle-leetcode-hard-d5e93557612c)



## Check Out this video

[![Video Explanation](https://img.youtube.com/vi/dAVF2NpC3j4/mqdefault.jpg)](https://youtu.be/dAVF2NpC3j4)





## Complexity Analysis

- **Time Complexity:** O(rows * cols), where `rows` is the number of rows and `cols` is the number of columns in the binary matrix.
- **Space Complexity:** O(cols), as we use an array to store the heights of bars for each row.

---
