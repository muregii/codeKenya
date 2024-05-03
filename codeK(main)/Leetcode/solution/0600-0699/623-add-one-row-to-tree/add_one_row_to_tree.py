# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def addOneRow(self, root, val, depth):
        """
        :type root: TreeNode
        :type val: int
        :type depth: int
        :rtype: TreeNode
        """
        if depth == 1:
            new_root = TreeNode(val)
            new_root.left = root
            return new_root

        def add_nodes(node, curr_depth):
            if not node:
                return

            if curr_depth == depth - 1:
                new_left = TreeNode(val)
                new_right = TreeNode(val)
                new_left.left = node.left
                new_right.right = node.right
                node.left = new_left
                node.right = new_right
            else:
                add_nodes(node.left, curr_depth + 1)
                add_nodes(node.right, curr_depth + 1)

        add_nodes(root, 1)
        return root
