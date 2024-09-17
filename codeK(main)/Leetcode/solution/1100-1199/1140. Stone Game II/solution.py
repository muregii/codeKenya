class Solution(object):
    def stoneGameII(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        n = len(piles)
        dp = [[0] * (n + 1) for _ in range(n)]
        suffix_sum = [0] * n
        suffix_sum[-1] = piles[-1]
        
        for i in range(n - 2, -1, -1):
            suffix_sum[i] = piles[i] + suffix_sum[i + 1]
        
        def helper(i, M):
            if i >= n:
                return 0
            if dp[i][M] != 0:
                return dp[i][M]
            
            max_stones = 0
            for X in range(1, 2 * M + 1):
                if i + X > n:
                    break
                max_stones = max(max_stones, suffix_sum[i] - helper(i + X, max(M, X)))
            
            dp[i][M] = max_stones
            return dp[i][M]
        
        return helper(0, 1)