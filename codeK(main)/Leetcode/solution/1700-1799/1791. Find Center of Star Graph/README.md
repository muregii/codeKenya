# Leetcode - Find Center of Star Graph

## Problem Description

There is an undirected **star** graph consisting of `n` **nodes** labeled from `1` to `n`. A star graph is a graph where there is one **center** node and **exactly** `n - 1` edges that connect the center node with every other node.

You are given a 2D integer array `edges` where each `edges[i] = [ui, vi]` indicates that there is an edge between the nodes `ui` and `vi`. Return the center of the given star graph.

**Constraints:**
- `3 <= n <= 10^5`
- `edges.length == n - 1`
- `edges[i].length == 2`
- `1 <= ui, vi <= n`
- `ui != vi`
- The given edges represent a valid star graph.

## Solution

To find the center of a star graph, identify the node that appears most frequently in the edges, as it will be connected to all other nodes.

1. **Understanding the Problem:**
   - In a star graph, there is one central node connected to all other `n-1` nodes.
   - Given a list of edges, the center node will appear in multiple edges.
   - We need to identify this node.

2. **Using Edge Analysis:**
   - In a star graph with `n` nodes, the center node will appear in `n-1` edges.
   - Given the constraints, the center node can be determined by examining the first two edges. The common node in these two edges will be the center node.

3. **Algorithm Steps:**
   - Extract the first two edges.
   - Compare the nodes in these edges to find the common node.
   - Return the common node as the center of the star graph.

### Example

Suppose you have the following edges:

```
edges = [[1, 2], [2, 3], [4, 2]]
```

By examining the first two edges:
- `[1, 2]`
- `[2, 3]`

The common node is `2`, which is the center of the star graph.

### Python Code

```python
class Solution(object):
    def findCenter(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        """
        
```

### Usage

To use the solution, create an instance of the `Solution` class and call the `findCenter` method with the `edges` array:

```python
solution = Solution()
edges = [[1, 2], [2, 3], [4, 2]]
result = solution.findCenter(edges)
print(result)  # Output: 2
```

### Additional Resources

[Link to detailed explanation on Algo Monster](https://algo.monster/liteproblems/1791)

[Link to detailed explanation on Medium](https://medium.com/@jjyk/leetcode-1791-find-center-of-star-graph-19ce1ca6f0aa)

### Check Out These Videos

[![Video Explanation](https://img.youtube.com/vi/XJ8l5ZOp6Js/mqdefault.jpg)](https://youtu.be/XJ8l5ZOp6Js)

[![Video Explanation](https://img.youtube.com/vi/KEKcW6eLyEY/mqdefault.jpg)](https://youtu.be/KEKcW6eLyEY)

[![Video Explanation](https://img.youtube.com/vi/QFFjjOGEQpU/mqdefault.jpg)](https://youtu.be/QFFjjOGEQpU)

### Complexity Analysis

- **Time Complexity:** O(1), as we only need to check the first two edges to determine the center.
- **Space Complexity:** O(1), as no additional space is required other than a few variables.