class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        nums = [1] + nums + [1]  # Build the new array with dummy balloons
        dp = [[0] * (n+2) for _ in range(n+2)]

        for left in range(n, -1, -1):
            for right in range(left+2, n+2):
                for i in range(left+1, right):
                    # For each balloon in subarray nums[left:right+1]
                    # try bursting it and take the maximum
                    dp[left][right] = max(dp[left][right], nums[left] * nums[i] * nums[right] + dp[left][i] + dp[i][right])

        return dp[0][n+1]