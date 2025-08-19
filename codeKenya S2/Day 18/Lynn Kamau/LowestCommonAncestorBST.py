#Lowest Common Ancestor in a Binary Search Tree LeetCode Challenge
#Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.
#According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

def lowest_common_ancestor(root, p, q):
    while root:
        if p.val < root.val and q.val < root.val:
            root = root.left
        elif p.val > root.val and q.val > root.val:
            root = root.right
        else:
            return root

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# usage
root = TreeNode(6, TreeNode(2, TreeNode(0), TreeNode(4)), TreeNode(8, TreeNode(7), TreeNode(9)))
p, q = root.left, root.right
print(lowest_common_ancestor(root, p, q).val)  # Output: 6

# Time Complexity: O(h) where h = height of tree
# Space Complexity: O(1)
