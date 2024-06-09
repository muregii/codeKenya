class Solution(object):
    def distributeCoins(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.moves = 0
        
        def dfs(node):
            if not node:
                return 0
            
            left_excess = dfs(node.left)
            right_excess = dfs(node.right)
            
            excess = node.val - 1 + left_excess + right_excess
            self.moves += abs(excess)
            
            return excess
        
        dfs(root)
        return self.moves