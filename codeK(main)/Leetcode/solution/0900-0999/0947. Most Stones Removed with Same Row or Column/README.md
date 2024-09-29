# Leetcode - Remove Stones to Minimize the Remaining Stones

## Problem Description

On a 2D plane, we place `n` stones at some integer coordinate points. Each coordinate point may have at most one stone.

A stone can be removed if it shares either the **same row or the same column** as another stone that has not been removed.

Given an array `stones` of length `n` where `stones[i] = [xi, yi]` represents the location of the `i-th` stone, *return the largest possible number of stones that can be removed.*

### Constraints:
- `1 <= stones.length <= 1000`
- `0 <= xi, yi <= 10^4`
- No two stones are at the same coordinate point.

## Solution

### Understanding the Problem:

The task is to maximize the number of stones that can be removed. We can only remove a stone if it shares the same row or column as another stone that remains in the grid. This problem can be framed as finding connected components in a graph, where stones are connected by their row or column.

### Breaking It Down:

1. **Graph Representation:**
   - Treat the stones as nodes in a graph.
   - Connect two nodes if they share the same row or the same column.

2. **Connected Components:**
   - Stones within the same connected component can be removed until one stone remains. The size of a connected component is the number of stones that can be removed.

3. **Union-Find Algorithm:**
   - We can use a union-find (disjoint set) data structure to identify and group connected components based on row and column connections.

### Algorithm Steps:

1. **Union-Find Data Structure:**
   - Create a union-find data structure to manage which stones are connected by row or column.

2. **Union Operation:**
   - For each stone, union its row and column with other stones in the same row or column.

3. **Count Components:**
   - Once we have grouped the stones into connected components, count the total number of stones and subtract the number of connected components to get the maximum number of stones that can be removed.

4. **Return the Result:**
   - Return the total number of stones minus the number of connected components.

### Python Code

```python
class Solution(object):
    def removeStones(self, stones):
        """
        :type stones: List[List[int]]
        :rtype: int
        """
        
```

### Example

```python
# Input:
stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]

# Output:
5
```

### Explanation:

1. The stones form a connected component based on their rows and columns.
2. We can remove all but one stone from this connected component, which results in removing 5 stones.

### Usage

To use this solution, create an instance of the `Solution` class and call the `removeStones` method with the `stones` list.

```python
solution = Solution()
stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
result = solution.removeStones(stones)
print(result)  # Output: 5
```

### Additional Resources

- [Link to detailed explanation on Algo Monster](https://algo.monster/liteproblems/947)

- [Link to GeeksforGeeks explanation](https://www.geeksforgeeks.org/remove-stones-to-minimize-the-number-of-stones/)

### Check Out These Video(s):

[![Video Explanation](https://img.youtube.com/vi/OwMNX8SPavM/mqdefault.jpg)](https://youtu.be/OwMNX8SPavM)

[![Video Explanation](https://img.youtube.com/vi/I1SMLOnhl2s/mqdefault.jpg)](https://youtu.be/I1SMLOnhl2s)

### Complexity Analysis

- **Time Complexity:** O(n), where `n` is the number of stones. Each stone is visited once, and the union-find operations are almost constant time.
- **Space Complexity:** O(n), for storing the parent pointers in the union-find structure.