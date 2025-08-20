# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: Optional[TreeNode]
        """
        inorder_map = {val: idx for idx, val in enumerate(inorder)}
        self.pre_idx = 0

        def array_to_tree(left, right):
            if left > right:
                return None

            # 1. Pick root from preorder
            root_val = preorder[self.pre_idx]
            self.pre_idx += 1
            root = TreeNode(root_val) # type: ignore

            # 2. Split inorder into left/right subtrees
            index = inorder_map[root_val]

            # 3. Build left and right subtrees recursively
            root.left = array_to_tree(left, index - 1)
            root.right = array_to_tree(index + 1, right)

            return root

        return array_to_tree(0, len(inorder) - 1)
