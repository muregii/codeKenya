class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        # Number of rows and columns
        m, n = len(points), len(points[0])
        
        # DP array for storing max points up to the current row
        dp = points[0][:]
        
        # Loop through each row starting from the second row
        for r in range(1, m):
            # Temp array to store max points for the current row
            new_dp = [0] * n
            
            # Left to right pass (to handle column shifts)
            left = [0] * n
            left[0] = dp[0]
            for c in range(1, n):
                left[c] = max(left[c - 1] - 1, dp[c])
            
            # Right to left pass
            right = [0] * n
            right[-1] = dp[-1]
            for c in range(n - 2, -1, -1):
                right[c] = max(right[c + 1] - 1, dp[c])
            
            # Update new_dp with the max from both directions
            for c in range(n):
                new_dp[c] = points[r][c] + max(left[c], right[c])
            
            # Update dp for the next row
            dp = new_dp[:]
        
        # Return the maximum points achievable after the last row
        return max(dp)