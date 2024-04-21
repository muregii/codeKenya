# Leetcode - Sum of Left Leaves

## Problem Description

Given `n` non-negative integers representing an elevation map where the width of each bar is `1`, compute how much water it can trap after raining.

Given the `root` of a binary tree, return the `sum of all the left leaves`.

A `leaf` is a node with no children. A `left leaf` is a leaf that is the left child of another node.


## Solution

The key to solving tree problems using Depth First Search (DFS) is to think from the perspective of a node instead of looking at the whole tree. This is in line with how recursion is written. Reason from a node's perspective, decide how the current node should be proceeded with, then recurse on children and let recursion take care of the rest.

When you are a node, the only things you know are `1)` your value and `2)` how to get to your children. So the recursive function you write manipulates these things.

Here's how we can calculate the sum of all the left leaves:

1. Start from the root of the tree.
2. Traverse the tree recursively.
3. At each node, check if its left child is a leaf.
4. If it's a leaf, add its value to the sum.
5. Otherwise, recursively traverse its left and right subtrees.

So now for example one the value will be 9 + 15 = 24

Does this make sense? Great!"


## Usage

To use the solution, simply create an instance of the `Solution` class and call the `sumOfLeftLeaves` method with the input root node of the binary tree:

```python
solution = Solution()
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

result = solution.sumOfLeftLeaves(root)
print(result)  # Output: 24
```


[Link to detailed explanation on Medium](https://medium.com/theleanprogrammer/404-sum-of-left-leaves-83e0a5a26ee1)

[Link to detailed explanation on Geeksforgeeks](https://www.geeksforgeeks.org/find-sum-left-leaves-given-binary-tree/)


## Check Out this video

[![Video Explanation](https://img.youtube.com/vi/eUgTTgpKMNA/mqdefault.jpg)](https://youtu.be/eUgTTgpKMNA)


[![Video Explanation](https://img.youtube.com/vi/RGDsjGz5MGk/mqdefault.jpg)](https://youtu.be/RGDsjGz5MGk)





## Complexity Analysis

- **Time Complexity:** O(n), where n is the number of nodes in the binary tree.
- **Space Complexity:** O(h), where h is the height of the binary tree, due to the recursive call stack.

---
