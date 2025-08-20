# Binary Tree Maximum Path Sum Leetcode Challenge
# Given the root of a non-empty binary tree, return the maximum path sum of any non-empty path.
# A path in a binary tree is a sequence of nodes where each pair of adjacent nodes has an edge connecting them.
# A node can not appear in the sequence more than once. The path does not necessarily need to include the root.
# The path sum of a path is the sum of the node's values in the path.

def max_path_sum(root):
    res = [root.val]
    def dfs(node):
        if not node:
            return 0
        left = max(dfs(node.left), 0)
        right = max(dfs(node.right), 0)
        res[0] = max(res[0], node.val + left + right)
        return node.val + max(left, right)
    dfs(root)
    return res[0]

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Test Case
root = TreeNode(-10, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
print(max_path_sum(root))

# Time Complexity: O(n)
# Space Complexity: O(h)
