# Leetcode - Sum of Distances in Tree

## Problem Description

There is an undirected connected tree with `n` nodes labeled from `0` to `n - 1` and `n - 1` edges.

You are given the integer `n` and the array `edges` where `edges[i] = [ai, bi]` indicates that there is an edge between nodes `ai` and `bi` in the tree.

Return an array `answer` of length `n` where `answer[i]` is the sum of the distances between the `ith` node in the tree and all other nodes.

## Solution

To solve this problem, we can perform two DFS traversals on the tree.

Here's how we can approach this problem:

1. First, we perform a DFS traversal to calculate two arrays: `count` and `res`.
   - `count[i]` represents the number of nodes in the subtree rooted at node `i`.
   - `res[i]` represents the sum of distances from node `i` to all other nodes in its subtree.
2. Then, we perform a second DFS traversal to update the `res` array based on the calculated `count` and `res` arrays.
   - For each edge `(u, v)`, where `u` is the parent of `v`, we update `res[v]` based on the values of `res[u]`, `count[u]`, `count[v]`, and the number of nodes in the remaining subtree.
3. After the second DFS traversal, the `res` array contains the sum of distances from each node to all other nodes.

## Usage

To use the solution, create an instance of the `Solution` class and call the `sumOfDistancesInTree` method with the input parameters `n` and `edges`:

```python
solution = Solution()
# Define the number of nodes and the edges of the tree
# n = 6
# edges = [[0,1],[0,2],[2,3],[2,4],[2,5]]
# Call the sumOfDistancesInTree method
result = solution.sumOfDistancesInTree(n, edges)
print(result)
```

```python
# n = 6
# edges = [[0,1],[0,2],[2,3],[2,4],[2,5]]
```
[Link to detailed explanation on Quora](https://www.quora.com/What-would-be-the-best-approach-to-find-the-distance-between-two-nodes-of-a-tree)


[Link to detailed explanation on Medium](https://dreamume.medium.com/leetcode-834-sum-of-distances-in-tree-523031b6a689)


[Link to detailed explanation on Geeksforgeeks](https://www.geeksforgeeks.org/find-distance-between-two-nodes-of-a-binary-tree/)



## Check Out this video

[![Video Explanation](https://img.youtube.com/vi/gmEsErNo84g/mqdefault.jpg)](https://youtu.be/gmEsErNo84g)


[![Video Explanation](https://img.youtube.com/vi/kM3A6AjHvjM/mqdefault.jpg)](https://youtu.be/kM3A6AjHvjM)


## Complexity Analysis

- **Time Complexity:** O(n), where n is the number of nodes in the tree. We perform two DFS traversals, each taking linear time.
- **Space Complexity:** O(n), where n is the number of nodes in the tree. We use additional space for the `count` and `res` arrays to store intermediate results.