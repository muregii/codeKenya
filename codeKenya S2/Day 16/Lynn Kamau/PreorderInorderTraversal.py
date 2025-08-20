#Construct Binary Tree from Preorder and Inorder Traversal LeetCode 105
# You are given two integer arrays preorder and inorder.
# Preorder is the preorder traversal of a binary tree
# Inorder is the inorder traversal of the same tree
# Both arrays are of the same size and consist of unique values.
# Rebuild the binary tree from the preorder and inorder traversals and return its root


def build_tree(preorder, inorder):
    if not preorder or not inorder:
        return None
    root_val = preorder.pop(0)
    root = TreeNode(root_val)
    idx = inorder.index(root_val)
    root.left = build_tree(preorder, inorder[:idx])
    root.right = build_tree(preorder, inorder[idx+1:])
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

    # 🔑 Trim trailing None values so output is clean
    while result and result[-1] is None:
        result.pop()

    print(result)

#Test Case
pre = [1,2,3,4]
ino = [2,1,3,4]
tree = build_tree(pre, ino)
print_tree(tree)

pre = [1]
ino = [1]
tree = build_tree(pre, ino)
print_tree(tree)



# Time Complexity: O(n^2)
# Space Complexity: O(n)
