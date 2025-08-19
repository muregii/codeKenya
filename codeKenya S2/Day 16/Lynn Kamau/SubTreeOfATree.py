#Subtree of Another Tree LeetCode Challenge
#Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.
#A subtree of a tree is a tree that consists of a node in the tree and all of this node's descendants.

def is_subtree(root, subRoot):
    if not root:
        return False
    if is_same(root, subRoot):
        return True
    return is_subtree(root.left, subRoot) or is_subtree(root.right, subRoot)

def is_same(p, q):
    if not p and not q:
        return True
    if not p or not q:
        return False
    return p.val == q.val and is_same(p.left, q.left) and is_same(p.right, q.right)

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#Example Usage
root = TreeNode(3, TreeNode(4, TreeNode(1), TreeNode(2)), TreeNode(5))
sub = TreeNode(4, TreeNode(1), TreeNode(2))
print(is_subtree(root, sub))  # Output: True

# Time Complexity: O(m * n)
# Space Complexity: O(h) where h = height of tree
