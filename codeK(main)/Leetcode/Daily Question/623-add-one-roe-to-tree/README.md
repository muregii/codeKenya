# Leetcode - Add One Row to Tree

## Problem Description

Given the `root` of a binary tree and two integers `val` and `depth`, add a row of nodes with value `val` at the given depth `depth`.

Note that the `root` node is at depth `1`.

The adding rule is as follows:

- Given the integer `depth`, for each non-null tree node `cur` at the depth `depth - 1`, create two tree nodes with value `val` as the left and right children of `cur`.
- The original left subtree of `cur` should be the left subtree of the new left child.
- The original right subtree of `cur` should be the right subtree of the new right child.
- If `depth == 1`, that means there is no depth `depth - 1` at all. In this case, create a tree node with value `val` as the new root of the original tree, and the original tree becomes the left subtree of the new root.



## Solution

To add a row of nodes with value `val` at the given depth `depth` in a binary tree, we can perform a depth-first search (DFS) traversal of the tree. At each node, we check if its depth is equal to `depth - 1`. If so, we add new nodes with value `val` as its children according to the adding rule. If the current depth is less than `depth - 1`, we continue traversing down the tree recursively. 

`DFS (Depth-first search) is a technique used for traversing trees or graphs. Here backtracking is used for traversal. In this traversal first, the deepest node is visited and then backtracks to its parent node if no sibling of that node exists`

Here's how we can implement this approach:

1. Perform a depth-first search (DFS) traversal of the binary tree.
2. At each node, check if its depth is equal to `depth - 1`.
3. If the depth is equal to `depth - 1`, add new nodes with value `val` as its children according to the adding rule.
4. If the current depth is less than `depth - 1`, continue traversing down the tree recursively.

This approach allows us to add a row of nodes with value `val` at the given depth `depth` in the binary tree efficiently.


Does this make sense? Great!"


## Usage

To use the solution, create an instance of the `Solution` class and call the `addOneRow` method with the input `root`, `val`, and `depth` representing the root of the binary tree, value to be added, and the depth at which the new row should be added, respectively:

```python
solution = Solution()
# Define the binary tree nodes
# root = TreeNode(val=1)
# root.left = TreeNode(val=2)
# root.right = TreeNode(val=3)
# ...
# Call the addOneRow method
result = solution.addOneRow(root, val, depth)
print(result)
```



## Check Out this video

[![Video Explanation](https://img.youtube.com/vi/Dmbisqlfo7Y/mqdefault.jpg)](https://youtu.be/Dmbisqlfo7Y)


[![Video Explanation](https://img.youtube.com/vi/o9_6bf6ZBnQ/mqdefault.jpg)](https://youtu.be/o9_6bf6ZBnQ)





### Complexity Analysis

- **Time Complexity:** O(n), where `n` is the number of nodes in the binary tree.
- The `addOneRow` function calls the `add_nodes` helper function, which recursively traverses the entire tree to find the nodes at the desired depth.
- In the worst case, we need to visit all nodes to reach the desired depth, resulting in a time complexity of O(n).

- **Space Complexity:** O(h), where `h` is the height of the binary tree. In the worst case, the space complexity can be O(n) for a skewed tree.
- The space complexity is determined by the recursive call stack in the `add_nodes` function.
- In the average case, the maximum depth of the recursion is equal to the height of the tree, leading to a space complexity of O(h).
- However, in the worst case of a skewed tree (where the tree is essentially a linked list), the height `h` becomes equal to the number of nodes `n`, resulting in a space complexity of O(n).

---

