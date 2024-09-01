# Leetcode - Regions Cut By Slashes

## Problem Description

An `n x n` grid is composed of `1 x 1` squares where each `1 x 1` square contains a `'/'`, `'\'`, or a blank space `' '`. These characters divide the square into contiguous regions.

Given the grid `grid` represented as a string array, return *the number of distinct regions*.

**Note** that backslash characters are escaped, so a `'\'` is represented as `'\\'`.


**Constraints:**
- `n == grid.length == grid[i].length`
- `1 <= n <= 30`
- `grid[i][j]` is either `'/'`, `'\'`, or `' '`.

## Solution

**Understanding the Problem:**
   - We need to determine the number of distinct regions formed by the slashes and spaces within the given grid.
   - Each slash (`'/'`) and backslash (`'\'`) divides a square into two regions. A blank space (`' '`) does not divide the square.

**Breaking It Down**
   - **Grid Representation:**
     - Each `1 x 1` square can be further divided into 4 smaller triangles (using a 3x3 grid for each square). This allows us to treat slashes and backslashes as boundaries between these smaller triangles.
     
   - **Union-Find (Disjoint Set) Approach:**
     - By representing each triangle in the grid as a node, we can use the Union-Find data structure to group connected components (regions).
     - We iterate over each square in the grid, merging triangles that are connected within the square or with adjacent squares.

**Implementation Approach:**
   - Create a Union-Find data structure to manage the merging of triangles within and across squares.
   - Iterate through the grid:
     - For each square, merge the triangles according to the slash or backslash present.
     - Merge triangles between adjacent squares (right and down).
   - Count the number of distinct regions by counting the number of distinct components in the Union-Find structure.

**Algorithm Steps:**
   - **Initialize Union-Find:** Create a Union-Find structure with `n * n * 4` elements (4 triangles per square).
   - **Process Each Square:** For each square, merge triangles based on the character (`'/'`, `'\'`, or `' '`).
   - **Merge Adjacent Squares:** Merge triangles between adjacent squares to connect regions.
   - **Count Regions:** The number of distinct regions corresponds to the number of distinct components in the Union-Find structure.

### Python Code

```python
class Solution(object):
    def regionsBySlashes(self, grid):
        """
        :type grid: List[str]
        :rtype: int
        """
        
```

### Example

```python
# Input
grid = [
  " /",
  "/ "
]

# Output
2
```

### Explanation
1. **Grid Representation:** 
   - The grid can be expanded to a 6x6 grid of triangles.
   - Slashes and backslashes divide this grid into different regions.
2. **Union-Find:** We use Union-Find to track and merge connected triangles, resulting in 2 distinct regions.

### Usage

To use the solution, create an instance of the `Solution` class and call the `regionsBySlashes` method with the `grid` parameter:

```python
# Example usage
solution = Solution()
grid = [
  " /",
  "/ "
]
result = solution.regionsBySlashes(grid)
print(result)  # Output: 2
```

### Additional Resources

[Link to detailed explanation on Algo Monster](https://algo.monster/liteproblems/regions-cut-by-slashes)

[Link to detailed explanation on Algo Monster](https://algo.monster/liteproblems/959)

[Link to detailed explanation on Medium](https://algomonster.medium.com/leetcode-959-regions-cut-by-slashes-865bf9a066c3)

### Check Out These Video(s)

[![Video Explanation](https://img.youtube.com/vi/tIZkh7mpIDo/mqdefault.jpg)](https://youtu.be/tIZkh7mpIDo)

[![Video Explanation](https://img.youtube.com/vi/j8KrBYIxHK8/mqdefault.jpg)](https://youtu.be/j8KrBYIxHK8)

### Complexity Analysis

- **Time Complexity:** O(n^2), where `n` is the grid size. This accounts for the processing of each square in the grid.
- **Space Complexity:** O(n^2), for the Union-Find structure storing the parent and rank of each node.