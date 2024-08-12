# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def delNodes(self, root, to_delete):
        """
        :type root: TreeNode
        :type to_delete: List[int]
        :rtype: List[TreeNode]
        """
        to_delete_set = set(to_delete)
        remaining_forest = []

        def helper(node, is_root):
            if not node:
                return None
            root_deleted = node.val in to_delete_set
            if is_root and not root_deleted:
                remaining_forest.append(node)
            node.left = helper(node.left, root_deleted)
            node.right = helper(node.right, root_deleted)
            return None if root_deleted else node

        helper(root, True)
        return remaining_forest