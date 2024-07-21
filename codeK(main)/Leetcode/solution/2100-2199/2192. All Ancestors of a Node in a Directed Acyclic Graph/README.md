# Leetcode - All Ancestors of a Node in a Directed Acyclic Graph

## Problem Description

You are given a positive integer `n` representing the number of nodes of a **Directed Acyclic Graph** (DAG). The nodes are numbered from `0` to `n - 1` (**inclusive**).

You are also given a 2D integer array `edges`, where `edges[i] = [fromi, toi]` denotes that there is a **unidirectional** edge from `fromi` to `toi` in the graph.

Return *a list `answer`, where `answer[i]` is the **list of ancestors** of the `i-th` node, sorted in **ascending order***.

A node `u` is an **ancestor** of another node `v` if `u` can reach `v` via a set of edges.

**Constraints:**
- `1 <= n <= 1000`
- `0 <= edges.length <= min(2000, n * (n - 1) / 2)`
- `edges[i].length == 2`
- `0 <= fromi, toi <= n - 1`
- `fromi != toi`
- There are no duplicate edges.
- The graph is directed and acyclic.

## Solution

To find the ancestors of each node in a DAG, use Depth-First Search (DFS) to traverse the graph and keep track of each node's ancestors.

1. **Understanding the Problem:**
   - Find all ancestors for each node in a DAG.
   - An ancestor of a node `v` is any node `u` that has a path leading to `v`.

2. **Using DFS to Find Ancestors:**
   - For each node, perform a DFS to find all reachable nodes (descendants).
   - By reversing the graph (considering edges from child to parent), find all ancestors by performing a DFS from each node.

3. **Algorithm Steps:**
   - Create an adjacency list to represent the graph.
   - Reverse the graph to create edges from child to parent.
   - For each node, perform a DFS to find all ancestors.
   - Store the ancestors in a list and sort them in ascending order.

### Example

Suppose you have the following nodes and edges:

```
n = 4
edges = [[0, 1], [0, 2], [1, 2], [2, 3]]
```

- The graph can be represented as:
  - 0 -> 1
  - 0 -> 2
  - 1 -> 2
  - 2 -> 3

- The reversed graph:
  - 1 -> 0
  - 2 -> 0
  - 2 -> 1
  - 3 -> 2

- Ancestors for each node:
  - Node 0: []
  - Node 1: [0]
  - Node 2: [0, 1]
  - Node 3: [0, 1, 2]

### Python Code

```python
class Solution(object):
    def getAncestors(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[List[int]]
        """
        
```

### Usage

To use the solution, create an instance of the `Solution` class and call the `getAncestors` method with the number of nodes and the `edges` array:

```python
solution = Solution()
n = 4
edges = [[0, 1], [0, 2], [1, 2], [2, 3]]
result = solution.getAncestors(n, edges)
print(result)  # Output: [[], [0], [0, 1], [0, 1, 2]]
```

### Additional Resources

[Link to detailed explanation on Algo Monster](https://algo.monster/liteproblems/2192)

[Link to detailed explanation on GeeksforGeeks](https://www.geeksforgeeks.org/find-ancestors-of-each-node-in-the-given-graph/)

[Link to detailed explanation on Medium](https://medium.com/@hongjje.dev/leetcode-solution-2192-all-ancestors-of-a-node-in-a-directed-acyclic-graph-37a139b645aa)

### Check Out These Videos

[![Video Explanation](https://img.youtube.com/vi/XpQysL9CEbw/mqdefault.jpg)](https://youtu.be/XpQysL9CEbw)


### Complexity Analysis

- **Time Complexity:** O(n + m), where `n` is the number of nodes and `m` is the number of edges. We traverse each node and edge once.
- **Space Complexity:** O(n + m), for storing the graph, the ancestors, and the recursion stack.