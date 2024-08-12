# Leetcode - Step-by-Step Directions from a Binary Tree Node to Another

## Problem Description

You are given the root of a **binary tree** with `n` nodes. Each node is uniquely assigned a value from `1` to `n`. You are also given an integer `startValue` representing the value of the start node `s`, and a different integer `destValue` representing the value of the destination node `t`.

Find the **shortest path** starting from node `s` and ending at node `t`. Generate step-by-step directions for this path as a string consisting of only the **uppercase** letters `'L'`, `'R'`, and `'U'`. Each letter indicates a specific direction:
- `'L'` means to go from a node to its **left child** node.
- `'R'` means to go from a node to its **right child** node.
- `'U'` means to go from a node to its **parent** node.

Return *the step-by-step directions of the **shortest path** from node `s` to node `t`*.

**Constraints:**
- The number of nodes in the tree is `n`.
- `2 <= n <= 10^5`
- `1 <= Node.val <= n`
- All the values in the tree are **unique**.
- `1 <= startValue, destValue <= n`
- `startValue != destValue`

## Solution

To solve this problem, find the shortest path between two nodes in a binary tree and generate the corresponding directions as a string.

1. **Understanding the Problem:**
   - We are given a binary tree with unique values for each node.
   - The task is to find the shortest path between two nodes and return the path as a string of directions.
   - The directions include moving to a left child (`'L'`), a right child (`'R'`), or back to a parent (`'U'`).

2. **Simulating the Process:**
   - Break down the problem into finding the lowest common ancestor (LCA) of the two nodes, then determining the path from the `startValue` node to the LCA, and from the LCA to the `destValue` node.
   - The path from the `startValue` to the LCA will involve moving upwards (using `'U'`).
   - The path from the LCA to the `destValue` will involve moving left (`'L'`) or right (`'R'`).

3. **Algorithm Steps:**
   - Find the path from the root to the `startValue` node.
   - Find the path from the root to the `destValue` node.
   - Identify the common prefix in both paths (this represents the path to the LCA).
   - Remove the common prefix from both paths.
   - The final directions are formed by adding `'U'` for each remaining step in the `startValue` path (to move up to the LCA) and appending the steps from the LCA to the `destValue`.

### Example

Suppose you have:
- A binary tree with root `1` and the structure:
  ```
      1
     / \
    2   3
   / \
  4   5
  ```
- `startValue = 4`, `destValue = 5`

1. The path from `1` to `4` is `'LL'`.
2. The path from `1` to `5` is `'LR'`.
3. The common prefix is `'L'` (path to node `2` which is the LCA).
4. Directions from `4` to the LCA: `'U'`.
5. Directions from the LCA to `5`: `'R'`.
6. Final result: `'UR'`.

### Python Code

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getDirections(self, root, startValue, destValue):
        """
        :type root: Optional[TreeNode]
        :type startValue: int
        :type destValue: int
        :rtype: str
        """
        
```

### Usage

To use the solution, create an instance of the `Solution` class and call the `getDirections` method with the `root`, `startValue`, and `destValue`:

```python
# Example usage
solution = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
startValue = 4
destValue = 5
directions = solution.getDirections(root, startValue, destValue)
print(directions)  # Output: "UR"
```

### Additional Resources

[Link to detailed explanation on Algo Monster](https://algo.monster/liteproblems/2096)

[Link to detailed explanation on GeeksforGeeks](https://www.geeksforgeeks.org/step-by-step-shortest-path-from-source-node-to-destination-node-in-a-binary-tree/)

### Check Out These Videos

[![Video Explanation](https://img.youtube.com/vi/JegJNGcwtFg/mqdefault.jpg)](https://youtu.be/JegJNGcwtFg)

[![Video Explanation](https://img.youtube.com/vi/BPVP_8dr7-U/mqdefault.jpg)](https://youtu.be/BPVP_8dr7-U)

[![Video Explanation](https://img.youtube.com/vi/tZ3tUOrB790/mqdefault.jpg)](https://youtu.be/tZ3tUOrB790)

### Complexity Analysis

- **Time Complexity:** O(n), where `n` is the number of nodes in the tree. We need to traverse the tree to find the paths.
- **Space Complexity:** O(h), where `h` is the height of the tree, due to the recursion stack and path storage.