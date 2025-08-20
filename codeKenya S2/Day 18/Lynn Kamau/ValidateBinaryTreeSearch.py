#Validate Binary Search Tree LeetCode Challenge
#Given a binary tree, determine if it is a valid binary search tree (BST).
#A valid BST is defined as follows:
#1. The left subtree of a node contains only nodes with keys less than the node’s key.
#2. The right subtree of a node contains only nodes with keys greater than the node’s key.
#3. Both the left and right subtrees must also be binary search trees.  

def is_valid_bst(root, low=float("-inf"), high=float("inf")):
    if not root:
        return True
    if not (low < root.val < high):
        return False
    return is_valid_bst(root.left, low, root.val) and is_valid_bst(root.right, root.val, high)

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# usage
root = TreeNode(2, TreeNode(1), TreeNode(3))
print(is_valid_bst(root))

# Time Complexity: O(n)
# Space Complexity: O(h) where h = height of tree
