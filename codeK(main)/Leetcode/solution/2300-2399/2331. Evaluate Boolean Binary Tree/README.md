# Leetcode - Evaluate Boolean Binary Tree

## Problem Description

You are given the `root` of a **full binary** tree with the following properties:

- **Leaf nodes** have either the value `0` or `1`, where `0` represents `False` and `1` represents `True`.
- **Non-leaf nodes** have either the value `2` or `3`, where `2` represents the boolean `OR` and `3` represents the boolean AND.

The **evaluation** of a node is as follows:

- If the node is a leaf node, the evaluation is the **value** of the node, i.e., `True` or `False`.
- Otherwise, **evaluate** the node's two children and **apply** the boolean operation of its value with the children's evaluations.

Return *the boolean result of **evaluating** the `root` node.*

A **full binary tree** is a binary tree where each node has either 0 or 2 children. 

A **leaf node** is a node that has zero children.


**Constraints:**
- The number of nodes in the tree is in the range `[1, 1000]`.
- `0 <= Node.val <= 3`
- Every node has either `0` or `2` children.
- Leaf nodes have a value of `0` or `1`.
- Non-leaf nodes have a value of `2` or `3`.

## Solution

Use a recursive approach to evaluate the binary tree.


Think of a tree, but instead of leaves and branches, we have numbers and operations. The leaves at the bottom have either a 0 or a 1, which means False or True. The other parts of the tree (branches) have either a 2 or a 3, which means OR or AND. We need to find out what the tree says at the top by looking at the leaves and working our way up.


The `evaluateTree` method takes the root of a binary tree as input and returns the boolean result of evaluating the tree. It uses a recursive approach to evaluate the tree from the leaves up to the root.

1. **Define the Recursive Function:**
   - If the current node is a leaf node (no children), return its boolean value.
   - Otherwise, recursively evaluate the left and right children.
   - Apply the boolean operation (OR for 2, AND for 3) to the results of the left and right children.

2. **Base Case:**
   - If the node is a leaf, return its value as a boolean (`True` for 1, `False` for 0).

3. **Recursive Case:**
   - Evaluate the left and right children.
   - Apply the corresponding boolean operation (`OR` or `AND`).


```python

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def evaluateTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        
```

## Usage

To use the solution, create an instance of the `Solution` class and call the `evaluateTree` method with the root of the binary tree:

```python
solution = Solution()
# Constructing the tree
root = TreeNode(2, TreeNode(1), TreeNode(3, TreeNode(0), TreeNode(1)))
result = solution.evaluateTree(root)
print(result)  # Output: True
```
[Link to detailed explanation on AlgoMonster](https://algo.monster/liteproblems/2331)


[Link to detailed explanation on Medium](https://medium.com/codex/2331-evaluate-boolean-binary-tree-6d273ce0c3c7)


[Link to detailed explanation on Geeksforgeeks](https://www.geeksforgeeks.org/evaluation-of-expression-tree/)




## Check Out this videos

[![Video Explanation](https://img.youtube.com/vi/bFxdpk0ww-o/mqdefault.jpg)](https://youtu.be/bFxdpk0ww-o)


[![Video Explanation](https://img.youtube.com/vi/9a_cP54jn8Q/mqdefault.jpg)](https://youtu.be/9a_cP54jn8Q)


[![Video Explanation](https://img.youtube.com/vi/UsaJ-M-txbg/mqdefault.jpg)](https://youtu.be/UsaJ-M-txbg)



## Complexity Analysis

- **Time Complexity:** O(n), where n is the number of nodes in the tree. Each node is visited once during the recursion.
- **Space Complexity:** O(h), where h is the height of the tree. This is the space used by the recursion stack, which in the worst case is the height of the tree. For a balanced tree, the height is log(n).
