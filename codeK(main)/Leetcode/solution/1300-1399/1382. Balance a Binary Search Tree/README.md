# Leetcode - Balance a Binary Search Tree

## Problem Description

Given the `root` of a binary search tree (BST), return *a **balanced** binary search tree with the same node values*. If there is more than one answer, **return any of them**.

A binary search tree is **balanced** if the depth of the two subtrees of every node never differs by more than `1`.

**Constraints:**
- The number of nodes in the tree is in the range `[1, 10^4]`.
- `1 <= Node.val <= 10^5`

## Solution

To balance a BST, the goal is to ensure that for every node in the tree, the depth of its left and right subtrees differs by no more than 1. This can be achieved by first extracting all nodes from the BST in sorted order and then constructing a balanced BST from this sorted list of nodes.

1. **Understanding the Problem:**
   - Convert an unbalanced BST into a balanced one while maintaining the BST properties.
   - A BST is balanced if, for each node, the depth difference between its left and right subtrees is at most 1.

2. **Steps to Balance the BST:**
   - Perform an in-order traversal of the original BST to obtain a sorted list of node values.
   - Use the sorted list to construct a balanced BST recursively.

3. **Algorithm Steps:**
   - **Step 1:** Perform an in-order traversal to get the sorted list of node values.
   - **Step 2:** Use the sorted list to build a balanced BST:
     - The middle element of the list becomes the root of the BST.
     - Recursively do the same for the left half and right half of the list to build the left and right subtrees.

### Example

Suppose you have the following BST:

```
      1
       \
        2
         \
          3
           \
            4
```

After balancing, it might become:

```
      3
     / \
    2   4
   /
  1
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
    def balanceBST(self, root):
    
```

### Usage

To use the solution, create an instance of the `Solution` class and call the `balanceBST` method with the root of the BST:

```python
solution = Solution()
# Construct the BST
root = TreeNode(1)
root.right = TreeNode(2)
root.right.right = TreeNode(3)
root.right.right.right = TreeNode(4)

result = solution.balanceBST(root)
# The result is the root of the balanced BST
```

### Additional Resources

[Link to detailed explanation on Algo Monster](https://algo.monster/liteproblems/1382)

[Link to detailed explanation on Geeksforgeeks](https://www.geeksforgeeks.org/convert-normal-bst-balanced-bst/)

[Link to detailed explanation on Medium](https://jimmy-shen.medium.com/balanced-bst-avl-tree-2da0ca2c908d)

### Check Out These Videos

[![Video Explanation](https://img.youtube.com/vi/0K0uCMYq5ng/mqdefault.jpg)](https://youtu.be/0K0uCMYq5ng)

[![Video Explanation](https://img.youtube.com/vi/8d9tOlk7g9w/mqdefault.jpg)](https://youtu.be/8d9tOlk7g9w)

[![Video Explanation](https://img.youtube.com/vi/3yA3ngjoo28/mqdefault.jpg)](https://youtu.be/3yA3ngjoo28)

### Complexity Analysis

- **Time Complexity:** O(n), where `n` is the number of nodes in the tree. The complexity is dominated by the in-order traversal and the construction of the balanced BST.
- **Space Complexity:** O(n), for storing the list of node values and the call stack during the recursion.