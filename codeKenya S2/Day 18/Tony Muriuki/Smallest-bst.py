# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: int
        """
        self.count = 0
        self.result = None

        def inorder(node):
            if not node or self.result is not None:
                return
            
            inorder(node.left)
            
            self.count += 1
            if self.count == k:
                self.result = node.val
                return

            inorder(node.right)
        
        inorder(root)
        return self.result
