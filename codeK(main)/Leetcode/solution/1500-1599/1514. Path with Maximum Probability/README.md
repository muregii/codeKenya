# Leetcode - Path with Maximum Probability

## Problem Description

You are given an **undirected weighted graph** with `n` nodes (0-indexed), represented by an edge list where `edges[i] = [a, b]` is an undirected edge connecting the nodes `a` and `b` with a **probability of success** of traversing that edge `succProb[i]`.

Given two nodes `start` and `end`, find the path with the **maximum probability** of success to go from `start` to `end` and return its success probability.

If there is no path from `start` to `end`, return `0`. Your answer will be accepted if it differs from the correct answer by at most `1e-5`.

### Constraints:
- `2 <= n <= 10^4`
- `0 <= start, end < n`
- `start != end`
- `0 <= a, b < n`
- `a != b`
- `0 <= succProb.length == edges.length <= 2 * 10^4`
- `0 <= succProb[i] <= 1`
- There is at most one edge between every two nodes.

## Solution

### Understanding the Problem

The task is to find the path with the **maximum probability** of success between the `start` and `end` nodes in an undirected graph. Each edge between nodes has an associated probability of success for traversal, and we need to maximize the overall probability from `start` to `end`.

### Breaking It Down

1. **Graph Representation**:
   - The graph can be represented as an adjacency list where each node connects to other nodes with a given probability.

2. **Dijkstra-like Approach**:
   - We want to find the **maximum probability path**, so instead of minimizing distance (like in Dijkstra’s algorithm), we will **maximize the probability**.
   - The probability of a path is calculated by multiplying the probabilities of all edges on the path. Our goal is to maximize this product.

### Algorithm Steps

1. **Graph Construction**:
   - Construct the graph as an adjacency list where each edge is represented with its probability of success.

2. **Priority Queue (Max-Heap)**:
   - Use a priority queue to explore nodes, similar to Dijkstra’s algorithm.
   - Instead of tracking minimum distances, we track **maximum probabilities** and use a max-heap to prioritize nodes with higher probabilities.

3. **Relaxation of Edges**:
   - For each node, update the maximum probability to reach its neighboring nodes and add them to the priority queue.

4. **Return the Result**:
   - If the `end` node is reached, return the maximum probability. If not, return `0` indicating no path exists.

### Python Code

```python
import heapq

class Solution(object):
    def maxProbability(self, n, edges, succProb, start, end):
        """
        :type n: int
        :type edges: List[List[int]]
        :type succProb: List[float]
        :type start: int
        :type end: int
        :rtype: float
        """
        
```

### Example

```python
# Input:
n = 5
edges = [[0, 1], [1, 2], [2, 3], [0, 3], [1, 4]]
succProb = [0.5, 0.7, 0.8, 0.6, 0.9]
start = 0
end = 4

# Output:
result = solution.maxProbability(n, edges, succProb, start, end)
print(result)  # Output: 0.45
```

### Explanation

1. The graph has `5` nodes and edges with associated probabilities.
2. We want to find the path with the maximum probability from node `0` to node `4`.
3. The solution explores the nodes, calculating the maximum probability for each path, and returns the best one.

### Usage

To use this solution, create an instance of the `Solution` class and call the `maxProbability` method with the graph parameters:

```python
solution = Solution()
n = 5
edges = [[0, 1], [1, 2], [2, 3], [0, 3], [1, 4]]
succProb = [0.5, 0.7, 0.8, 0.6, 0.9]
start = 0
end = 4
result = solution.maxProbability(n, edges, succProb, start, end)
print(result)  # Output: 0.45
```

### Additional Resources

- [Detailed Explanation on Algo Monster](https://algo.monster/liteproblems/1514)

- [Detailed Explanation on Medium](https://medium.com/@_monitsharma/daily-leetcode-problems-problem-1514-path-with-maximum-probability-7adcc0bd99df)


### Check Out These Videos:

[![Video Explanation](https://img.youtube.com/vi/aPThR7YBCAM/mqdefault.jpg)](https://youtu.be/aPThR7YBCAM)

[![Video Explanation](https://img.youtube.com/vi/kPsDTGcrzGM/mqdefault.jpg)](https://youtu.be/kPsDTGcrzGM)

### Complexity Analysis

- **Time Complexity**: O((n + m) * log n), where `n` is the number of nodes, and `m` is the number of edges. This is because we use Dijkstra's algorithm with a priority queue.
- **Space Complexity**: O(n + m), to store the graph and additional data structures like the probability array and priority queue.