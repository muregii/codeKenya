# Leetcode - Delete Nodes and Return Forest

## Problem Description

Given the `root` of a binary tree, each node in the tree has a distinct value.

After deleting all nodes with a value in `to_delete`, we are left with a forest (a disjoint union of trees).

Return the roots of the trees in the remaining forest. You may return the result in any order.

**Constraints:**
- The number of nodes in the tree is at most `1000`.
- Each node has a distinct value between `1` and `1000`.
- `to_delete.length <= 1000`
- `to_delete` contains distinct values between `1` and `1000`.

## Solution

To solve this problem, the key is to traverse the tree and handle the deletion of nodes specified in `to_delete`. If a node is deleted, its children become the roots of new trees, and we need to keep track of these new roots.

1. **Understanding the Problem:**
   - We are given a binary tree with unique values for each node.
   - We need to delete specific nodes and return the roots of the remaining trees.
   - The resulting forest consists of all the trees that are disjoint after the deletion.

2. **Simulating the Process:**
   - Traverse the tree and for each node, check if it should be deleted.
   - If a node is deleted, add its left and right children (if they exist) as new roots of the forest.
   - Continue the traversal to handle the deletion of other nodes.

3. **Algorithm Steps:**
   - Use a recursive function to traverse the tree:
     - If the current node is `None`, return `None`.
     - Recursively process the left and right children.
     - If the current node needs to be deleted:
       - If the left child exists, add it to the list of new roots.
       - If the right child exists, add it to the list of new roots.
       - Return `None` to delete the current node.
     - If the node is not deleted, return the current node to maintain the tree structure.
   - The root itself may or may not be deleted, so it is handled separately by adding it to the list of roots if it is not deleted.

### Example

Suppose you have:
- A binary tree with the root `1` and the structure:
  ```
        1
       / \
      2   3
     / \   \
    4   5   6
  ```
- `to_delete = [3, 5]`

1. Process the tree:
   - Node `3` is deleted, so node `6` becomes a new root.
   - Node `5` is deleted, and it has no children.
2. The resulting forest:
   - Trees rooted at nodes `1`, `2`, `4`, and `6`.

### Python Code

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def delNodes(self, root, to_delete):
        
```

### Usage

To use the solution, create an instance of the `Solution` class and call the `delNodes` method with the `root` of the binary tree and the list of nodes to delete:

```python
# Example usage
solution = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)
to_delete = [3, 5]
forest = solution.delNodes(root, to_delete)

# Output will be a list of TreeNode objects representing the roots of the remaining trees.
```

### Additional Resources

[Link to detailed explanation on Algo Monster](https://algo.monster/liteproblems/1110)

[Link to detailed explanation on GeeksforGeeks](https://www.geeksforgeeks.org/print-the-forests-of-a-binary-tree-after-removal-of-given-nodes/)

### Check Out These Videos

[![Video Explanation](https://img.youtube.com/vi/aaSFzFfOQ0o/mqdefault.jpg)](https://youtu.be/aaSFzFfOQ0o)

[![Video Explanation](https://img.youtube.com/vi/FQ7HuXTM-KA/mqdefault.jpg)](https://youtu.be/FQ7HuXTM-KA)

[![Video Explanation](https://img.youtube.com/vi/UhKu0q1yXHY/mqdefault.jpg)](https://youtu.be/UhKu0q1yXHY)

### Complexity Analysis

- **Time Complexity:** O(n), where `n` is the number of nodes in the tree. We need to traverse each node to determine if it should be deleted and process its children accordingly.
- **Space Complexity:** O(h), where `h` is the height of the tree, due to the recursion stack used during the traversal.