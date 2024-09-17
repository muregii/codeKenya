# Leetcode - Binary Tree Postorder Traversal

## Problem Description

Given the `root` of a binary tree, return *the postorder traversal of its nodes' values*.

**Constraints:**
- The number of nodes in the tree is in the range `[0, 100]`.
- `-100 <= Node.val <= 100`

## Solution

### Understanding the Problem:
- The task is to perform a **postorder traversal** on a binary tree, meaning we need to visit:
  1. The left subtree first.
  2. Then the right subtree.
  3. Finally, the root node.
  
This traversal order ensures that for each subtree, both its child nodes are processed before the subtree's root node.

### Breaking It Down:
- **Recursive Approach:** One common way to solve this problem is through recursion.
  - Recursively visit the left subtree.
  - Recursively visit the right subtree.
  - Add the root node's value to the result list.
  
This recursive process mirrors the postorder traversal structure.

- **Iterative Approach:** Another approach is using a stack to simulate recursion, as recursion can sometimes be less efficient for large trees.

### Algorithm Steps:
1. **Base Case:** If the root is `None`, return an empty list.
2. **Recursive Function:** 
   - Recursively traverse the left subtree.
   - Recursively traverse the right subtree.
   - Append the root's value to the result.
3. **Return the Result:** The final list should contain the postorder traversal of the tree.

### Python Code

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
```

### Example

```python
# Input
root = [1, null, 2, 3]  # Tree structure where root is 1, right child is 2, left child of 2 is 3.

# Output
[3, 2, 1]  # Postorder traversal visits left, right, and then root.

# Explanation:
# 1. Visit the left subtree of root (1), which is empty.
# 2. Visit the right subtree of root (1), which has root (2).
# 3. Visit the left subtree of root (2), which is (3).
# 4. Finally, add the value of root nodes in reverse order of traversal.
```

### Usage

To use this solution, create an instance of the `Solution` class and call the `postorderTraversal` method with the root of the binary tree as the input.

```python
# Example usage
solution = Solution()
root = TreeNode(1, None, TreeNode(2, TreeNode(3)))
result = solution.postorderTraversal(root)
print(result)  # Output: [3, 2, 1]
```

### Additional Resources

[Link to detailed explanation on Algo Monster](https://algo.monster/liteproblems/145)

[Link to a detailed walkthrough on GeeksforGeeks](https://www.geeksforgeeks.org/tree-traversals-inorder-preorder-and-postorder/)

[Link to a detailed walkthrough on GeeksforGeeks](hhttps://www.geeksforgeeks.org/postorder-traversal-of-binary-tree/)


## Check Out this video

[![Video Explanation](https://img.youtube.com/vi/PiqIXedWhoY/mqdefault.jpg)](https://youtu.be/PiqIXedWhoY)


[![Video Explanation](https://img.youtube.com/vi/B6XTLPpsW7k/mqdefault.jpg)](https://youtu.be/B6XTLPpsW7k)

### Complexity Analysis

- **Time Complexity:** O(n), where `n` is the number of nodes in the tree. Each node is visited once during the traversal.
- **Space Complexity:** O(n) in the worst case due to the recursion stack (if the tree is unbalanced) or the use of a result list of size `n`.