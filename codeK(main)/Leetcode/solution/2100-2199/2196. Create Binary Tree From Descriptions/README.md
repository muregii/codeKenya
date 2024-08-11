# Leetcode - Create Binary Tree from Descriptions

## Problem Description

You are given a 2D integer array `descriptions` where `descriptions[i] = [parent_i, child_i, isLeft_i]` indicates that `parent_i` is the **parent** of `child_i` in a **binary** tree of **unique** values.

- If `isLeft_i == 1`, then `child_i` is the left child of `parent_i`.
- If `isLeft_i == 0`, then `child_i` is the right child of `parent_i`.

Construct the binary tree described by `descriptions` and return *its **root***.

The test cases are generated such that the binary tree is **valid**.

**Constraints:**
- `1 <= descriptions.length <= 10^4`
- `descriptions[i].length == 3`
- `1 <= parent_i, child_i <= 10^5`
- `0 <= isLeft_i <= 1`
- The binary tree described by `descriptions` is valid.

## Solution

To solve this problem, construct a binary tree based on the parent-child relationships described in the `descriptions` array. The key is to track each node's parent and child relationships to determine the tree's structure.

1. **Understanding the Problem:**
   - We are given relationships in the form of `(parent, child, isLeft)`.
   - Each entry in the descriptions tells us whether a child node is a left or right child of a parent node.
   - Construct the binary tree and identify the root node.

2. **Simulating the Process:**
   - Use dictionaries to store nodes and track the parent-child relationships.
   - For each description, create or retrieve the parent and child nodes and establish the left or right connection.
   - Identify the root node, which will be the only node that is not a child of any other node.

3. **Algorithm Steps:**
   - Initialize a dictionary to store nodes by their values.
   - Initialize a set to keep track of all child nodes.
   - For each description:
     - Create or retrieve the parent and child nodes.
     - Establish the left or right connection based on the `isLeft` value.
     - Add the child node to the set of child nodes.
   - The root node will be the node that is not in the set of child nodes.
   - Return the root node.

### Example

Suppose you have:
- `descriptions = [[1, 2, 1], [1, 3, 0], [2, 4, 1]]`

1. Process the descriptions:
   - `1` is the parent of `2` (left child).
   - `1` is the parent of `3` (right child).
   - `2` is the parent of `4` (left child).
2. Identify `1` as the root node since it is not a child of any node.

### Python Code

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def createBinaryTree(self, descriptions):
        """
        :type descriptions: List[List[int]]
        :rtype: Optional[TreeNode]
        """
        
```

### Usage

To use the solution, create an instance of the `Solution` class and call the `createBinaryTree` method with the `descriptions` list:

```python
# Example usage
solution = Solution()
descriptions = [[1, 2, 1], [1, 3, 0], [2, 4, 1]]
root = solution.createBinaryTree(descriptions)
```

### Additional Resources

[Link to detailed explanation on Algo Monster](https://algo.monster/liteproblems/2196)

[Link to detailed explanation on Medium](https://medium.com/@everythingismindgame/2196-create-binary-tree-from-descriptions-acac8eef67b2)

[Link to detailed explanation on GeeksforGeeks](https://www.geeksforgeeks.org/construct-complete-binary-tree-given-array/)

### Check Out These Videos

[![Video Explanation](https://img.youtube.com/vi/yWkrFfqO7NA/mqdefault.jpg)](https://youtu.be/yWkrFfqO7NA)

[![Video Explanation](https://img.youtube.com/vi/Sg0hiTM85AI/mqdefault.jpg)](https://youtu.be/Sg0hiTM85AI)

### Complexity Analysis

- **Time Complexity:** O(n), where `n` is the number of descriptions. We process each description exactly once.
- **Space Complexity:** O(n), due to the use of dictionaries to store nodes and child relationships.