
# Leetcode - Determine Valid Path in a Bi-Directional Graph

## Problem Description

You are given a bi-directional graph with `n` vertices, where each vertex is labeled from `0` to `n - 1` (inclusive). The edges in the graph are represented as a 2D integer array `edges`, where each `edges[i] = [ui, vi]` denotes a bi-directional edge between vertex `ui` and vertex `vi`. Every vertex pair is connected by at most one edge, and no vertex has an edge to itself.

You want to determine if there is a valid path that exists from vertex `source` to vertex `destination`.

Given `edges` and the integers `n`, `source`, and `destination`, return `true` if there is a valid path from `source` to `destination`, or `false` otherwise.

## Solution

To solve this problem, we can perform a Depth-First Search (DFS) traversal or Breadth-First Search (BFS) traversal starting from the source vertex. During the traversal, we mark visited vertices to avoid revisiting them and explore all possible paths until we either reach the destination vertex or exhaust all paths.

Here's how we can approach this problem:

1. Initialize a boolean array `visited` of size `n` to keep track of visited vertices.
2. Implement a DFS or BFS traversal function that takes the current vertex as input and explores its adjacent vertices recursively or iteratively.
3. Mark the current vertex as visited.
4. For each adjacent vertex of the current vertex, if it has not been visited yet, recursively call the DFS function with the adjacent vertex as the current vertex or enqueue the adjacent vertex in the BFS traversal queue.
5. If the DFS or BFS traversal reaches the destination vertex, return `true`.
6. If the DFS or BFS traversal exhausts all possible paths from the source vertex without reaching the destination vertex, return `false`.

By performing DFS or BFS traversal starting from the source vertex, we can determine if there exists a valid path to reach the destination vertex in the given bi-directional graph.

## Usage

To use the solution, create an instance of the `Solution` class and call the `validPath` method with the input parameters `n`, `edges`, `source`, and `destination`:

```python
solution = Solution()
# Define the graph edges, number of vertices, source vertex, and destination vertex
# edges = [[0,1],[1,2],[2,0]]
# n = 3
# source = 0
# destination = 2
# Call the validPath method
result = solution.validPath(n, edges, source, destination)
print(result)
```

```python
# edges = [[0,1],[1,2],[2,0]]
# n = 3
# source = 0
# destination = 2
```


[Link to detailed explanation](https://algodaily.com/lessons/implementing-graphs-edge-list-adjacency-list-adjacency-matrix)


[Link to detailed explanation on Geeksforgeeks](https://yuminlee2.medium.com/breadth-first-search-bfs-algorithm-b93ef5258c4d)


## Check Out this video

[![Video Explanation](https://img.youtube.com/vi/qhmdBndZnk0/mqdefault.jpg)](https://youtu.be/qhmdBndZnk0)


## Complexity Analysis

- **Time Complexity:** O(V + E), where V is the number of vertices and E is the number of edges in the graph. We perform a DFS or BFS traversal to explore the graph, visiting each vertex and edge once.
- **Space Complexity:** O(V), where V is the number of vertices in the graph. We use additional space for the `visited` array or the queue in the BFS traversal to keep track of visited vertices.

