# Leetcode - Distribute Coins in Binary Tree

## Problem Description

You are given the `root` of a binary tree with `n` nodes where each `node` in the tree has `node.val` coins. There are `n` coins in total throughout the whole tree.

In one move, we may choose two adjacent nodes and move one coin from one node to another. A move may be from parent to child, or from child to parent.

Return *the **minimum** number of moves required to make every node have **exactly** one coin*.

**Constraints:**
- The number of nodes in the tree is `n`.
- `1 <= n <= 100`
- `0 <= Node.val <= n`
- The sum of all `Node.val` is `n`.

## Solution

Use a recursive approach to distribute the coins in the binary tree.

Think of a tree in your yard, but instead of leaves, the tree has coins hanging on it. Each branch can have a different number of coins. We want to make sure each branch has exactly one coin. To do this, we can move coins from one branch to another, but each move takes some effort. Our goal is to do this in the least number of moves.


The `distributeCoins` method takes the root of a binary tree as input and returns the minimum number of moves required to distribute the coins such that each node has exactly one coin. It uses a recursive approach to traverse the tree and balance the coins.

1. **Define the Recursive Function:**
   - The recursive function `dfs` calculates the balance of coins for each subtree.
   - It returns the number of excess coins at each node (positive if the node has more coins than needed, negative if fewer).

2. **Base Case:**
   - If the node is `None`, return `0` because there's no coin to distribute.

3. **Recursive Case:**
   - Recursively call the function on the left and right children.
   - Calculate the total moves required by summing the absolute values of the balances of the left and right children.
   - Return the balance of the current node adjusted by its children's balances and its own coin value.

4. **Calculate Moves:**
   - Initialize the total moves to `0`.
   - Call the recursive function `dfs` starting from the root.


We start at the root of the tree and move coins around to ensure each node has exactly one coin. We use a helper function to calculate how many coins need to be moved for each node. This function goes down to the leaves and works its way back up to the root, keeping track of the number of moves needed.


```python

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def distributeCoins(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
```

## Usage

To use the solution, create an instance of the `Solution` class and call the `distributeCoins` method with the root of the binary tree:

```python
solution = Solution()
# Constructing the tree
root = TreeNode(3, TreeNode(0), TreeNode(0))
result = solution.distributeCoins(root)
print(result)  # Output: 2
```

[Link to detailed explanation on AlgoMonster](https://algo.monster/liteproblems/979)

[Link to detailed explanation on Medium](https://medium.com/coding-memo/leetcode-distribute-coins-in-binary-tree-7029323db443)

[Link to detailed explanation on Geeksforgeeks](https://www.geeksforgeeks.org/distribute-candies-in-a-binary-tree/)


## Check Out this videos

[![Video Explanation](https://img.youtube.com/vi/YfdfIOeV_RU/mqdefault.jpg)](https://youtu.be/YfdfIOeV_RU)

[![Video Explanation](https://img.youtube.com/vi/MfXxic8IhkI/mqdefault.jpg)](https://youtu.be/MfXxic8IhkI)

[![Video Explanation](https://img.youtube.com/vi/RkVF5PdZJ1w/mqdefault.jpg)](https://youtu.be/RkVF5PdZJ1w)



## Complexity Analysis

- **Time Complexity:** O(n), where n is the number of nodes in the tree. Each node is visited once during the recursion.
- **Space Complexity:** O(h), where h is the height of the tree. This is the space used by the recursion stack, which in the worst case is the height of the tree. For a balanced tree, the height is log(n).
