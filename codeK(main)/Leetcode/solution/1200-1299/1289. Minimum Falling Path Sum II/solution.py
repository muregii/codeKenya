class Solution(object):
    def minFallingPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        dp = [[0] * n for _ in range(n)]
        
        # Initialize the first row of dp
        for j in range(n):
            dp[0][j] = grid[0][j]
        
        # Fill in the remaining rows of dp
        for i in range(1, n):
            for j in range(n):
                dp[i][j] = grid[i][j] + min(dp[i-1][k] for k in range(n) if k != j)
        
        # Return the minimum value in the last row of dp
        return min(dp[n-1])