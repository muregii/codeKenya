# Leetcode - Remove Max Number of Edges to Keep Graph Fully Traversable

## Problem Description

Alice and Bob have an undirected graph of `n` nodes and three types of edges:

- **Type 1:** Can be traversed by Alice only.
- **Type 2:** Can be traversed by Bob only.
- **Type 3:** Can be traversed by both Alice and Bob.

Given an array `edges` where `edges[i] = [typei, ui, vi]` represents a bidirectional edge of type `typei` between nodes `ui` and `vi`, find the maximum number of edges you can remove so that after removing the edges, the graph can still be fully traversed by both Alice and Bob. The graph is fully traversed by Alice and Bob if starting from any node, they can reach all other nodes.

Return *the maximum number of edges you can remove, or return `-1` if Alice and Bob cannot fully traverse the graph*.

**Constraints:**
- `1 <= n <= 10^5`
- `1 <= edges.length <= min(10^5, 3 * n * (n - 1) / 2)`
- `edges[i].length == 3`
- `1 <= typei <= 3`
- `1 <= ui < vi <= n`
- All tuples `(typei, ui, vi)` are distinct.

## Solution

To solve this problem, ensure that both Alice and Bob can traverse the entire graph independently. This involves using union-find (disjoint-set) data structures to manage connected components and determine which edges are redundant.

1. **Understanding the Problem:**
   - We need to ensure both Alice and Bob can fully traverse the graph.
   - We want to remove the maximum number of edges while still allowing full traversal.

2. **Union-Find Data Structures:**
   - Use two union-find structures, one for Alice and one for Bob, to track connectivity.
   - Handle type 3 edges first (usable by both Alice and Bob) to maximize shared connections.

3. **Algorithm Steps:**
   - Initialize two union-find structures for Alice and Bob.
   - Process type 3 edges first to merge nodes in both Alice's and Bob's union-find structures.
   - Process type 1 and type 2 edges to merge nodes in their respective union-find structures.
   - Count the number of edges used and calculate the number of edges that can be removed.
   - Check if both Alice and Bob can traverse all nodes. If not, return -1.

### Example

Suppose you have the following nodes and edges:

```
n = 4
edges = [[3, 1, 2], [3, 2, 3], [1, 1, 3], [2, 3, 4]]
```

- Type 3 edges: [3, 1, 2] and [3, 2, 3]
- Type 1 edge: [1, 1, 3]
- Type 2 edge: [2, 3, 4]

- After processing type 3 edges, Alice and Bob have the following connections:
  - Alice: 1-2, 2-3 (connected components: {1, 2, 3})
  - Bob: 1-2, 2-3 (connected components: {1, 2, 3})

- Process type 1 edge for Alice:
  - Alice: 1-2, 2-3, 1-3 (connected components: {1, 2, 3})

- Process type 2 edge for Bob:
  - Bob: 1-2, 2-3, 3-4 (connected components: {1, 2, 3, 4})

- Alice cannot reach node 4, so return -1.

### Python Code

```python
class Solution(object):
    def maxNumEdgesToRemove(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        
```

### Usage

To use the solution, create an instance of the `Solution` class and call the `maxNumEdgesToRemove` method with the number of nodes and the `edges` array:

```python
solution = Solution()
n = 4
edges = [[3, 1, 2], [3, 2, 3], [1, 1, 3], [2, 3, 4]]
result = solution.maxNumEdgesToRemove(n, edges)
print(result)  # Output: -1
```

### Additional Resources

[Link to detailed explanation on Algo Monster](https://algo.monster/liteproblems/1579)

[Link to detailed explanation on Medium](https://medium.com/@_monitsharma/daily-leetcode-problems-problem-1579-remove-max-number-of-edges-to-keep-graph-fully-traversable-3e276f9d85ed)


### Check Out These Videos

[![Video Explanation](https://img.youtube.com/vi/booGwg5wYm4/mqdefault.jpg)](https://youtu.be/booGwg5wYm4)

[![Video Explanation](https://img.youtube.com/vi/ukLyFDlBFW0/mqdefault.jpg)](https://youtu.be/ukLyFDlBFW0)

### Complexity Analysis

- **Time Complexity:** O(E log V), where `E` is the number of edges and `V` is the number of nodes. This accounts for sorting the edges and performing union-find operations.
- **Space Complexity:** O(V), for storing the parent and rank arrays in the union-find data structures.