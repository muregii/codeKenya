# Serialize and Deserialize Binary Tree Leetcode Challenge
# Implement an algorithm to serialize and deserialize a binary tree.
# Serialization is the process of converting an in-memory structure into a sequence of bits so that it can be stored or sent across a network to be reconstructed later in another computer environment.
# You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure. 
# There is no additional restriction on how your serialization/deserialization algorithm should work.

def serialize(root):
    vals = []
    def dfs(node):
        if not node:
            vals.append("N")
            return
        vals.append(str(node.val))
        dfs(node.left)
        dfs(node.right)
    dfs(root)
    return ",".join(vals)

def deserialize(data):
    vals = data.split(",")
    self_iter = iter(vals)
    def dfs():
        val = next(self_iter)
        if val == "N":
            return None
        node = TreeNode(int(val))
        node.left = dfs()
        node.right = dfs()
        return node
    return dfs()

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Example Usage
root = TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4), TreeNode(5)))
data = serialize(root)
print(data) 
tree = deserialize(data)
print(serialize(tree))  

# Time Complexity: O(n)
# Space Complexity: O(n)


