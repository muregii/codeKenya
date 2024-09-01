# Leetcode - Spiral Matrix III

## Problem Description

You start at the cell `(rStart, cStart)` of a `rows x cols` grid facing east. The northwest corner is at the first row and column in the grid, and the southeast corner is at the last row and column.

You will walk in a **clockwise spiral shape** to visit every position in this grid. Whenever you move outside the grid's boundary, you continue your walk outside the grid (but may return to the grid boundary later). Eventually, you reach all `rows * cols` spaces of the grid.

Return *an array of coordinates representing the positions of the grid in the order you visited them*.

**Constraints:**
- `1 <= rows, cols <= 100`
- `0 <= rStart < rows`
- `0 <= cStart < cols`

## Solution

**Understanding the Problem:**
   - The task is to simulate walking in a spiral pattern on a grid, starting from a given position.
   - The spiral movement involves moving right (east), down (south), left (west), and up (north) in cycles, gradually increasing the step size after every two turns.

**Breaking It Down**
   - **Movement Pattern:**
     - Start by moving to the right. After every two movements (right, down), increase the number of steps taken by one.
     - The movement directions are repeated in the order: right, down, left, and up.
     - Continue this pattern until all grid positions are visited.
     
   - **Handling Boundaries:**
     - If a movement goes outside the grid, skip that move and continue to the next one, but count the steps as taken.
     - Make sure to consider the entire spiral even when parts of it are outside the grid.

**Implementation Approach:**
   - Track the current position and direction.
   - Use a loop to simulate the movement in the spiral, changing direction and increasing step count as needed.
   - Collect the coordinates of the cells visited within the grid.
   - Continue the process until all grid cells are visited.

**Algorithm Steps:**
   - **Initialize Position and Direction:** Start at `(rStart, cStart)` facing right (east).
   - **Simulate Movement:** Move in the current direction, adjusting steps and direction after every two turns.
   - **Check Grid Boundaries:** If a position is within the grid, add it to the result list.
   - **Repeat Until Done:** Continue the spiral movement until all positions are visited.
   - **Return Result:** Return the list of visited coordinates.

### Python Code

```python
class Solution(object):
    def spiralMatrixIII(self, rows, cols, rStart, cStart):
        """
        :type rows: int
        :type cols: int
        :type rStart: int
        :type cStart: int
        :rtype: List[List[int]]
        """
       
```

### Example

```python
# Input
rows = 5
cols = 6
rStart = 1
cStart = 4

# Output
[[1, 4], [1, 5], [2, 5], [2, 4], [2, 3], [1, 3], [0, 3], [0, 4], [0, 5], [3, 5], [3, 4], [3, 3], [3, 2], [2, 2], [1, 2], [0, 2], [4, 5], [4, 4], [4, 3], [4, 2], [3, 1], [2, 1], [1, 1], [0, 1], [4, 1], [4, 0], [3, 0], [2, 0], [1, 0], [0, 0]]
```

### Explanation
1. **Starting Point:** Begin at `(1, 4)` facing east.
2. **Spiral Movement:** The movement follows a spiral pattern, extending in length after each full cycle of right, down, left, and up movements.
3. **Result:** The output list contains the coordinates of each cell visited in the order of the spiral.

### Usage

To use the solution, create an instance of the `Solution` class and call the `spiralMatrixIII` method with the `rows`, `cols`, `rStart`, and `cStart` parameters:

```python
# Example usage
solution = Solution()
rows = 5
cols = 6
rStart = 1
cStart = 4
result = solution.spiralMatrixIII(rows, cols, rStart, cStart)
print(result)
```

### Additional Resources

[Link to detailed explanation on Algo Monster](https://algo.monster/liteproblems/885)

[Link to detailed explanation on Medium](https://medium.com/nerd-for-tech/leetcode-spiral-matrix-60d7568b50ca)

[Link to detailed explanation on Geeksforgeeks](https://www.geeksforgeeks.org/form-a-spiral-matrix-from-the-given-array/)

[Link to detailed explanation on Geeksforgeeks](https://www.geeksforgeeks.org/print-a-given-matrix-in-spiral-form/)

### Check Out These Video(s)

[![Video Explanation](https://img.youtube.com/vi/0qep3f9cqVs/mqdefault.jpg)](https://youtu.be/0qep3f9cqVs)

[![Video Explanation](https://img.youtube.com/vi/Xf5Zm5Y8PKM/mqdefault.jpg)](https://youtu.be/Xf5Zm5Y8PKM)


### Complexity Analysis

- **Time Complexity:** O(rows * cols), as each cell in the grid is visited exactly once.
- **Space Complexity:** O(rows * cols), for storing the result list.