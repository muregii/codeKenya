# Leetcode - Modify Graph Edge Weights

## Problem Description

You are given an **undirected weighted connected** graph containing `n` nodes labeled from `0` to `n-1`, and an integer array `edges` where `edges[i] = [ai, bi, wi]` indicates that there is an edge between nodes `ai` and `bi` with weight `wi`.

Some edges have a weight of `-1` (representing an unknown weight), while others have a **positive** weight (`wi > 0`).

The task is to modify all edges with a weight of `-1` by assigning them **positive integer values** in the range `[1, 2 * 10^9]` such that the **shortest distance** between the nodes `source` and `destination` becomes equal to an integer `target`. If there are multiple ways to modify the graph, any correct solution will be accepted.

Return *an array containing all edges (even unmodified ones) in any order if it is possible to make the shortest distance from `source` to `destination` equal to `target`, or an **empty array** if it's impossible.*

Note: You are not allowed to modify the weights of edges with initial positive weights.

### Constraints

- `1 <= n <= 100`
- `1 <= edges.length <= n * (n - 1) / 2`
- `edges[i].length == 3`
- `0 <= ai, bi < n`
- `wi = -1 or 1 <= wi <= 10^7`
- `ai != bi`
- `0 <= source, destination < n`
- `source != destination`
- `1 <= target <= 10^9`
- The graph is connected, and there are no self-loops or repeated edges.

## Solution

### Understanding the Problem

The task is to modify the graph's edges such that the shortest path between `source` and `destination` becomes equal to a given `target`. The challenge here is that some edges have unknown weights (represented by `-1`), and we must assign appropriate values to those weights without affecting other constraints.

### Breaking It Down

1. **Graph Representation**:
   - The graph is represented as an adjacency list where each edge has a weight.
   - We are tasked with modifying edges that have weights of `-1`.

2. **Shortest Path Calculation**:
   - The key to solving this problem is to compute the shortest path from `source` to `destination`.
   - We will use a shortest path algorithm like Dijkstra’s to calculate distances while considering edge modifications.

3. **Edge Modification**:
   - For edges with weight `-1`, we can assign positive values in the range `[1, 2 * 10^9]`.
   - The goal is to assign these values in such a way that the shortest path equals `target`.

### Algorithm Steps

1. **Initial Graph Setup**:
   - Construct the graph with the given edges, treating `-1` weighted edges as unknown.

2. **Dijkstra's Algorithm**:
   - Use Dijkstra's algorithm to calculate the shortest path between `source` and `destination` while treating unknown weights as a variable.

3. **Edge Modification**:
   - Modify the `-1` weighted edges such that the shortest path between `source` and `destination` equals `target`.

4. **Check for Feasibility**:
   - If it is possible to modify the weights to achieve the `target` distance, return the modified graph.
   - If not, return an empty array.

### Python Code

```python
class Solution(object):
    def modifiedGraphEdges(self, n, edges, source, destination, target):
        """
        :type n: int
        :type edges: List[List[int]]
        :type source: int
        :type destination: int
        :type target: int
        :rtype: List[List[int]]
        """
```

### Example

```python
# Input:
n = 5
edges = [[0, 1, -1], [1, 2, 4], [2, 3, -1], [3, 4, 3], [0, 4, 7]]
source = 0
destination = 4
target = 10

# Output:
# Any valid solution where the modified edge weights result in the shortest path from source to destination being 10.

solution = Solution()
edges_modified = solution.modifiedGraphEdges(n, edges, source, destination, target)
print(edges_modified)
```

### Explanation

1. The graph contains nodes with weighted edges, some of which have weights `-1` (unknown).
2. We need to assign values to these unknown edges such that the shortest path between node `0` and node `4` equals `10`.
3. After calculating the modified edges, we return the updated graph.

### Usage

To use the solution, create an instance of the `Solution` class and call the `modifiedGraphEdges` method with the graph parameters.

```python
solution = Solution()
edges_modified = solution.modifiedGraphEdges(n, edges, source, destination, target)
print(edges_modified)
```

### Additional Resources

- [Detail Explanation on Algo Monster](https://algo.monster/liteproblems/2699)

- [Detail Explanation on Medium](https://medium.com/@Sourabh_Gurav/modify-graph-edge-weights-73dff97e81b5)

- [Detail Explanation on Geeksforgeeks](https://www.geeksforgeeks.org/shortest-path-weighted-graph-weight-edge-1-2/)

### Check Out These Videos

[![Video Explanation](https://img.youtube.com/vi/bS5K1UXe8WI/mqdefault.jpg)](https://youtu.be/bS5K1UXe8WI)

[![Video Explanation](https://img.youtube.com/vi/LaNoqRHRD18/mqdefault.jpg)](https://youtu.be/LaNoqRHRD18)

### Complexity Analysis

- **Time Complexity**: O(n * log(n) + m), where `n` is the number of nodes, and `m` is the number of edges. This is because we use Dijkstra’s algorithm to calculate the shortest path.
- **Space Complexity**: O(n + m) for storing the graph and additional data structures.