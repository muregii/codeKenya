
---

# Leetcode - Find Farmland

## Problem Description

You are given a 0-indexed `m x n` binary matrix `land` where a `0` represents a hectare of forested land and a `1` represents a hectare of farmland.

To keep the land organized, there are designated rectangular areas of hectares that consist entirely of farmland. These rectangular areas are called groups. No two groups are adjacent, meaning farmland in one group is not four-directionally adjacent to another farmland in a different group.

`land` can be represented by a coordinate system where the top left corner of land is `(0, 0)` and the bottom right corner of land is `(m-1, n-1)`. Find the coordinates of the top left and bottom right corner of each group of farmland. A group of farmland with a top left corner at `(r1, c1)` and a bottom right corner at `(r2, c2)` is represented by the 4-length array `[r1, c1, r2, c2]`.

Return a 2D array containing the 4-length arrays described above for each group of farmland in `land`. If there are no groups of farmland, return an empty array. You may return the answer in any order.

## Solution

To solve this problem, we can iterate through each cell in the `land` matrix. Whenever we encounter a `1`, we perform a depth-first search (DFS) to explore the entire group of farmland connected to that cell. During the DFS traversal, we keep track of the minimum and maximum row and column indices of the farmland group.

Here's how we can approach this problem:

1. Iterate through each cell in the `land` matrix.
2. If the current cell contains farmland (`land[i][j] == 1`) and has not been visited yet, perform a DFS traversal to explore the entire farmland group connected to that cell.
3. During the DFS traversal, keep track of the minimum and maximum row and column indices of the farmland group.
4. Once the DFS traversal is complete, add the coordinates of the top left and bottom right corners of the farmland group to the result array.
5. Repeat this process for all cells in the `land` matrix.

By performing DFS traversals for each group of farmland, we can determine the coordinates of the top left and bottom right corners of each group.

## Usage

To use the solution, create an instance of the `Solution` class and call the `findFarmland` method with the input `land` representing the binary matrix:

```python
solution = Solution()
# Define the binary matrix representing the land
# land = [[1,0,0,1,0],
#         [1,0,1,0,0],
#         [0,0,1,0,1],
#         [0,0,0,1,1]]
# Call the findFarmland method
result = solution.findFarmland(land)
print(result)
```

```python
# land = [[1,0,0,1,0],
#         [1,0,1,0,0],
#         [0,0,1,0,1],
#         [0,0,0,1,1]]
```

## Check Out this video

[![Video Explanation](https://img.youtube.com/vi/XdQCVYaC84o/mqdefault.jpg)](https://youtu.be/XdQCVYaC84o)


## Complexity Analysis

- **Time Complexity:** O(m * n), where m is the number of rows and n is the number of columns in the `land` matrix. We visit each cell once during the DFS traversal.
- **Space Complexity:** O(1), excluding the space required for the output array. We are using only a constant amount of extra space for storing temporary variables during the DFS traversal.

---  