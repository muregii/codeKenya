class Solution(object):
    def evaluateTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        if root.left is None and root.right is None:
            # Leaf node
            return bool(root.val)
        
        left_eval = self.evaluateTree(root.left)
        right_eval = self.evaluateTree(root.right)
        
        if root.val == 2:
            # OR operation
            return left_eval or right_eval
        else:
            # AND operation
            return left_eval and right_eval