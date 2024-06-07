# Leetcode - Remove Leaf Nodes with Target Value

## Problem Description

Given the `root` of a binary tree and an integer `target`, delete all the **leaf nodes** with the value `target`. 

Note that once you delete a leaf node with the value `target`, if its parent node becomes a leaf node and has the value `target`, it should also be deleted (you need to continue doing that until you cannot).

**Constraints:**
- The number of nodes in the tree is in the range `[1, 3000]`.
- `1 <= Node.val, target <= 1000`

## Solution

Use a recursive approach to delete the leaf nodes with the target value.


Think of a tree in your backyard. Now, imagine that the leaves of the tree have numbers on them. We want to remove all the leaves that have a certain number. But there's a catch! After we remove those leaves, if the branch that was holding those leaves becomes a leaf itself and has the same number, we need to remove it too. We keep doing this until we can't remove any more leaves.



The `removeLeafNodes` method takes the root of a binary tree and a target value as input and returns the root of the tree after removing all the leaf nodes with the target value. It uses a recursive approach to traverse the tree and remove the target leaf nodes.

1. **Define the Recursive Function:**
   - If the current node is `None`, return `None`.
   - Recursively call the function on the left and right children.
   - After processing the children, check if the current node is a leaf and its value equals the target.
   - If it is, return `None` to delete it.
   - Otherwise, return the current node.

2. **Base Case:**
   - If the node is `None`, return `None`.

3. **Recursive Case:**
   - Process the left and right children.
   - Check if the current node should be deleted and return the appropriate value.


We start at the root of the tree and look at its children. We use a helper function that goes down the tree and checks each node. If a node is a leaf and its value matches the target, we remove it. If removing a leaf makes its parent a leaf with the same value, we remove the parent too. We continue this process until there are no more leaves to remove.


```python

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def removeLeafNodes(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: TreeNode
        """
       
```

## Usage

To use the solution, create an instance of the `Solution` class and call the `removeLeafNodes` method with the root of the binary tree and the target value:

```python
solution = Solution()
# Constructing the tree
root = TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(2), TreeNode(4, TreeNode(2), TreeNode(5))))
target = 2
result = solution.removeLeafNodes(root, target)
# Function to print the tree in order for verification
def print_tree(node):
    if not node:
        return
    print_tree(node.left)
    print(node.val)
    print_tree(node.right)

print_tree(result)  # Output: 1, 3, 4, 5
```
[Link to detailed explanation on AlgoMonster](https://algo.monster/liteproblems/1325)


[Link to detailed explanation on Medium](https://yash-soni.medium.com/solving-leetcode-problem-1325-delete-leaves-with-a-given-value-bee1613ed56e)


[Link to detailed explanation on Geeksforgeeks](https://www.geeksforgeeks.org/delete-leaf-nodes-value-x/)




## Check Out this videos

[![Video Explanation](https://img.youtube.com/vi/Ir7MIOREBsc/mqdefault.jpg)](https://youtu.be/Ir7MIOREBsc)


[![Video Explanation](https://img.youtube.com/vi/FqAoYAwbwV8/mqdefault.jpg)](https://youtu.be/FqAoYAwbwV8)


[![Video Explanation](https://img.youtube.com/vi/sLgrWTOQSGs/mqdefault.jpg)](https://youtu.be/sLgrWTOQSGs)


## Complexity Analysis

- **Time Complexity:** O(n), where n is the number of nodes in the tree. Each node is visited once during the recursion.
- **Space Complexity:** O(h), where h is the height of the tree. This is the space used by the recursion stack, which in the worst case is the height of the tree. For a balanced tree, the height is log(n).