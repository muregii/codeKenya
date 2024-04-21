# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.sum = 0
        self.dfs(root, False)
        return self.sum

    def dfs(self, node, is_left):
        if not node:
            return

        if node.left is None and node.right is None and is_left:
            self.sum += node.val

        self.dfs(node.left, True)
        self.dfs(node.right, False)
