# Leetcode - Binary Search Tree to Greater Sum Tree

## Problem Description

Given the `root` of a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST is changed to the original key plus the sum of all keys greater than the original key in the BST.

As a reminder, a *binary search tree* is a tree that satisfies these constraints:
- The left subtree of a node contains only nodes with keys **less than** the node's key.
- The right subtree of a node contains only nodes with keys **greater than** the node's key.
- Both the left and right subtrees must also be binary search trees.

**Constraints:**
- The number of nodes in the tree is in the range `[1, 100]`.
- `0 <= Node.val <= 100`
- All the values in the tree are **unique**.

## Solution

To convert the BST to a Greater Tree, use a reverse in-order traversal (right -> node -> left). This traversal ensures that we process nodes from the largest to the smallest. Maintain a cumulative sum while traversing the tree to update each node's value accordingly.

1. **Understanding the Problem:**
   - In a Greater Tree, each node's value is updated to the original value plus the sum of all values greater than the node's value in the BST.
   - We use a reverse in-order traversal to achieve this, maintaining a running sum to keep track of the accumulated values.

2. **Using a Reverse In-Order Traversal:**
   - Traverse the right subtree first to process larger values.
   - Update the current node's value with the cumulative sum.
   - Traverse the left subtree to process smaller values.

3. **Algorithm Steps:**
   - Initialize a variable to keep track of the cumulative sum.
   - Perform a reverse in-order traversal of the BST.
   - For each node, update its value with the cumulative sum and add the node's original value to the cumulative sum.
   - Continue this process until all nodes have been updated.

### Example

Suppose you have the following BST:

```
       4
      / \
     1   6
    / \ / \
   0  2 5  7
         \
          3
           \
            8
```

After converting it to a Greater Tree, the BST becomes:

```
      30
      / \
    36   21
   / \  / \
  36 35 26 15
        \
         33
          \
           8
```

### Python Code


```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def bstToGst(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        
```

### Usage

To use the solution, create an instance of the `Solution` class and call the `bstToGst` method with the root of the BST:

```python
solution = Solution()
# Construct the BST
root = TreeNode(4)
root.left = TreeNode(1)
root.right = TreeNode(6)
root.left.left = TreeNode(0)
root.left.right = TreeNode(2)
root.left.right.right = TreeNode(3)
root.right.left = TreeNode(5)
root.right.right = TreeNode(7)
root.right.right.right = TreeNode(8)

result = solution.bstToGst(root)
# The result is the root of the modified Greater Tree
```

### Additional Resources

[Link to detailed explanation on Algo Monster](https://algo.monster/liteproblems/1038)

[Link to detailed explanation on GeeksforGeeks](https://www.geeksforgeeks.org/convert-bst-to-a-binary-tree/)

[Link to detailed explanation on Medium](https://medium.com/nerd-for-tech/convert-bst-to-greater-tree-day-72-python-1d1e4c7e3364)

### Check Out These Videos

[![Video Explanation](https://img.youtube.com/vi/9Aw18-yQs6o/mqdefault.jpg)](https://youtu.be/9Aw18-yQs6o)

[![Video Explanation](https://img.youtube.com/vi/7vVEJwVvAlI/mqdefault.jpg)](https://youtu.be/7vVEJwVvAlI)

[![Video Explanation](https://img.youtube.com/vi/4nnl3FrwEYM/mqdefault.jpg)](https://youtu.be/4nnl3FrwEYM)

### Complexity Analysis

- **Time Complexity:** O(n), where `n` is the number of nodes in the tree. Each node is visited exactly once during the traversal.
- **Space Complexity:** O(h), where `h` is the height of the tree. This space is used by the call stack during the recursion. In the worst case, the height of the tree is equal to the number of nodes, resulting in O(n) space complexity.