# Leetcode - Minimum Height Trees

## Problem Description

A tree is an undirected graph in which any two vertices are connected by exactly one path. In other words, any connected graph without simple cycles is a tree.

Given a tree of `n` nodes labelled from `0 to n - 1`, and an array of `n - 1` `edges` where `edges[i] = [ai, bi]`indicates that there is an undirected edge between the two nodes `ai` and `bi` in the tree, you can choose any node of the tree as the root. When you select a node `x` as the root, the result tree has height `h`. Among all possible rooted trees, those with minimum height (i.e. `min(h)`)  are called `minimum height trees (MHTs)`.

Return a `list of all MHTs' root` labels. You can return the answer in any order.

The height of a rooted tree is the number of edges on the longest downward path between the root and a leaf.

## Solution

To solve this problem, we can use a topological sorting approach combined with BFS. We start by finding the leaves of the tree and removing them along with their corresponding edges. We repeat this process until we are left with either one or two nodes, which represent the roots of the minimum height trees.

Here's how we can approach this problem:

1. Construct an adjacency list to represent the tree using the given edges.
2. Initialize a queue with all the leaf nodes (nodes with only one neighbor).
3. Remove the leaves from the tree along with their corresponding edges and update the degrees of their neighbors.
4. Add the new leaves (nodes with updated degree equal to 1) to the queue.
5. Repeat steps 3-4 until there are either one or two nodes left in the queue, which represent the roots of the minimum height trees.

By repeatedly removing the leaves of the tree, we can find the roots of the minimum height trees.

## Usage

To use the solution, create an instance of the `Solution` class and call the `findMinHeightTrees` method with the input parameters `n` and `edges`:

```python
solution = Solution()
# Define the number of nodes and the edges of the tree
# n = 6
# edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]
# Call the findMinHeightTrees method
result = solution.findMinHeightTrees(n, edges)
print(result)
```

```python
# n = 6
# edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]
```


[Link to detailed explanation](https://leetcode.ca/2016-10-05-310-Minimum-Height-Trees/)


## Check Out this video

[![Video Explanation](https://img.youtube.com/vi/wQGQnyv_9hI/mqdefault.jpg)](https://youtu.be/wQGQnyv_9hI)


[![Video Explanation](https://img.youtube.com/vi/ivl6BHJVcB0/mqdefault.jpg)](https://youtu.be/ivl6BHJVcB0)


## Complexity Analysis

- **Time Complexity:** O(N), where N is the number of nodes in the tree. We perform a BFS traversal to find the leaves and remove them, which takes linear time.
- **Space Complexity:** O(N), where N is the number of nodes in the tree. We use additional space for the adjacency list, queue, and result list.