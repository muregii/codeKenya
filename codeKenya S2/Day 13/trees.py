class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def left_most(root):
        if not root:
                return None
        if not root.left:
              return root

        return left_most(root.left)
        #while root.left:
        #        root = root.left
        #  return root.val
root1 = TreeNode(1,
                TreeNode(2,
                        TreeNode(4),
                        TreeNode(3)),
                TreeNode(5))
leftmost = left_most(root1)

print(leftmost.val)