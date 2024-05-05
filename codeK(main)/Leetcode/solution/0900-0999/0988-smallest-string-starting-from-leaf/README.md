# Leetcode - Smallest String Starting From Leaf

## Problem Description

You are given the `root` of a binary tree where each node has a value in the range `[0, 25]` representing the letters `'a'` to `'z'`.

Return the lexicographically smallest string that starts at a leaf of this tree and ends at the root.

As a reminder, any shorter prefix of a string is lexicographically smaller.

For example, `"ab"` is lexicographically smaller than `"aba"`.
A leaf of a node is a node that has no children.


## Solution

The problem involves finding the lexicographically smallest string that starts at a leaf of the given binary tree and ends at the root. We can solve this problem using a depth-first search (DFS) traversal of the binary tree.

Here's how we can approach this problem:

1. We perform a depth-first search (DFS) traversal of the binary tree.
2. During the traversal, we construct strings representing the paths from the leaves to the root.
3. At each leaf node, we append the corresponding letter to the string.
4. Once we reach the root node, we return the constructed string representing the lexicographically smallest path from a leaf to the root.

By performing a DFS traversal and constructing strings for each path from a leaf to the root, we can find the lexicographically smallest string that satisfies the given conditions.


Does this make sense? Great!"


## Usage

To use the solution, simply create an instance of the `Solution` class and call the `smallestFromLeaf` method with the input `root` representing the root of the binary tree:

```python
solution = Solution()
# Define the binary tree nodes
# root = TreeNode(val=1)
# root.left = TreeNode(val=2)
# root.right = TreeNode(val=3)
# ...
# Call the smallestFromLeaf method
result = solution.smallestFromLeaf(root)
print(result)
```

```python
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```


[Link to detailed explanation](https://algo.monster/liteproblems/988)


[Link to detailed explanation on Geeksforgeeks](https://www.geeksforgeeks.org/pairwise-swap-leaf-nodes-binary-tree/)




## Check Out this video


[![Video Explanation](https://img.youtube.com/vi/UvdWfxQ_ZDs/mqdefault.jpg)](https://youtu.be/UvdWfxQ_ZDs)





## Complexity Analysis

- **Time Complexity:** O(n), where n is the number of nodes in the binary tree.
- **Space Complexity:** O(h), where h is the height of the binary tree. In the worst case, the space complexity can be O(n) for a skewed tree.

---

