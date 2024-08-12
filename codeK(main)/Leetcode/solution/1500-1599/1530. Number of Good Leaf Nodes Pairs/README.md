# Leetcode - Number of Good Leaf Nodes Pairs

## Problem Description

You are given the `root` of a binary tree and an integer `distance`. A pair of two different **leaf** nodes of the binary tree is considered "good" if the length of **the shortest** path between them is less than or equal to `distance`.

Return *the number of good leaf node pairs in the tree*.

**Constraints:**
- The number of nodes in the tree **is in the range** `[1, 210]`.
- `1 <= Node.val <= 100`
- `1 <= distance <= 10`

## Solution

To solve this problem, traverse the tree and find pairs of leaf nodes that satisfy the condition where the distance between them is less than or equal to the given `distance`.

1. **Understanding the Problem:**
   - The binary tree contains nodes, where some of them are leaf nodes (nodes without children).
   - A "good" pair of leaf nodes is one where the shortest path between the two nodes is less than or equal to the given `distance`.
   - We need to count the number of such pairs.

2. **Simulating the Process:**
   - To find the "good" pairs, we can perform a post-order traversal of the tree.
   - For each node, we can calculate the distances to all leaf nodes in its left and right subtrees.
   - We then check if there exist pairs of leaf nodes (one from the left subtree and one from the right subtree) where the sum of their distances to the current node is less than or equal to the given `distance`.
   - If such pairs exist, we count them as "good" pairs.

3. **Algorithm Steps:**
   - Use a recursive function to traverse the tree in a post-order manner.
   - For each node, collect the distances to all leaf nodes in its left and right subtrees.
   - For every leaf node in the left subtree, check if there exists a leaf node in the right subtree such that the sum of their distances to the current node is less than or equal to the given `distance`.
   - Accumulate the count of such pairs and propagate the information up the tree.

### Example

Suppose you have:
- A binary tree with the root `1` and the structure:
  ```
        1
       / \
      2   3
     /     \
    4       5
           / \
          6   7
  ```
- `distance = 3`

1. Process the tree:
   - Leaf nodes: `4`, `6`, `7`
   - Good leaf node pairs: `(6, 7)`, since their distance is `2` which is less than or equal to `3`.

2. The result is `1` (one good pair).

### Python Code

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def countPairs(self, root, distance):
        
```

### Usage

To use the solution, create an instance of the `Solution` class and call the `countPairs` method with the `root` of the binary tree and the `distance` value:

```python
# Example usage
solution = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(4)
root.right = TreeNode(3)
root.right.right = TreeNode(5)
root.right.right.left = TreeNode(6)
root.right.right.right = TreeNode(7)
distance = 3
good_pairs = solution.countPairs(root, distance)
print(good_pairs)  # Output: 1
```

### Additional Resources

[Link to detailed explanation on Algo Monster](https://algo.monster/liteproblems/1530)

[Link to detailed explanation on Medium](https://medium.com/@ghoshshroddha/1530-number-of-good-leaf-nodes-pairs-leetcode-f67117e95837)

[Link to detailed explanation on Geeksforgeeks](https://www.geeksforgeeks.org/count-pairs-of-leaf-nodes-in-a-binary-tree-which-are-at-most-k-distance-apart/)

### Check Out These Videos

[![Video Explanation](https://img.youtube.com/vi/f_epkBeS1LQ/mqdefault.jpg)](https://youtu.be/f_epkBeS1LQ)

[![Video Explanation](https://img.youtube.com/vi/6IFTcv5WZkA/mqdefault.jpg)](https://youtu.be/6IFTcv5WZkA)

[![Video Explanation](https://img.youtube.com/vi/hA408ZMan1Q/mqdefault.jpg)](https://youtu.be/hA408ZMan1Q)

### Complexity Analysis

- **Time Complexity:** O(n), where `n` is the number of nodes in the tree. We need to traverse each node and check the distances to leaf nodes.
- **Space Complexity:** O(h), where `h` is the height of the tree, due to the recursion stack used during the traversal and the space needed to store distances to leaf nodes.