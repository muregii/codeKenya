#Invert Binary Tree Leetcode Problem
#Given the root of a binary tree, invert the tree, and return its root.
#A binary tree is inverted if all left and right children are swapped at every node.

def invert_tree(root):
    if not root:
        return None
    root.left, root.right = invert_tree(root.right), invert_tree(root.left)
    return root

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def print_tree(root):
    if not root:
        return []
    result, queue = [], [root]
    while queue:
        node = queue.pop(0)
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)

    # ✅ Only new part: remove trailing None values
    while result and result[-1] is None:
        result.pop()

    print(result)

# usage
root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7, TreeNode(6), TreeNode(9)))
inverted = invert_tree(root)
print_tree(inverted)  # Output: [4, 7, 2, 9, 6, 3, 1]

# Time Complexity: O(n)
# Space Complexity: O(h) where h = height of tree

