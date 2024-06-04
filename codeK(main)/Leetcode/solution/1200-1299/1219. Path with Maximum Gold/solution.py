class Solution(object):
    def getMaximumGold(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        self.max_gold = 0
        
        def dfs(i, j, gold):
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == 0:
                return
            
            gold += grid[i][j]
            self.max_gold = max(self.max_gold, gold)
            
            temp = grid[i][j]
            grid[i][j] = 0  # Mark as visited
            
            dfs(i + 1, j, gold)  # Down
            dfs(i - 1, j, gold)  # Up
            dfs(i, j + 1, gold)  # Right
            dfs(i, j - 1, gold)  # Left
            
            grid[i][j] = temp  # Restore the value
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] > 0:
                    dfs(i, j, 0)
        
        return self.max_gold