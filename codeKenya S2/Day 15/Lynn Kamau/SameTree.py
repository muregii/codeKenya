#Same Binary Tree Leetcode Problem
#Given the roots of two binary trees p and q, return true if the trees are equivalent, otherwise return false.
#Two binary trees are considered equivalent if they share the exact same structure and the nodes have the same values.

def is_same_tree(p, q):
    if not p and not q:
        return True
    if not p or not q:
        return False
    return p.val == q.val and is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# usage
p = TreeNode(1, TreeNode(2), TreeNode(3))
q = TreeNode(1, TreeNode(2), TreeNode(3))
print(is_same_tree(p, q))  # Output: True

# Time Complexity: O(n)
# Space Complexity: O(h) where h = height of tree