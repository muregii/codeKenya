#kth smallest element in a BST LeetCode Challenge
#Given a binary search tree (BST), write a function to find the kth smallest element in it.
#You may assume k is always valid, 1 ≤ k ≤ BST's total elements.


def kth_smallest(root, k):
    stack = []
    while True:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        k -= 1
        if k == 0:
            return root.val
        root = root.right

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# usage
root = TreeNode(3, TreeNode(1, None, TreeNode(2)), TreeNode(4))
print(kth_smallest(root, 1))  # Output: 1

# Time Complexity: O(h + k)
# Space Complexity: O(h)
