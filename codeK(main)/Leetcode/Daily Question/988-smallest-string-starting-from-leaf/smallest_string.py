class Solution(object):
    def smallestFromLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: str
        """
        self.result = "~"  # Initialize with a large string

        def dfs(node, path):
            if not node:
                return

            # Construct the path string by appending the current node's value
            path = chr(node.val + ord('a')) + path

            # If we reached a leaf node, check if the current path is smaller than the result
            if not node.left and not node.right:
                self.result = min(self.result, path)
            else:
                # Explore the left and right subtrees
                dfs(node.left, path)
                dfs(node.right, path)

        dfs(root, "")
        return self.result
