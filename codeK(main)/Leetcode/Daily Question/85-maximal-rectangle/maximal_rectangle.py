class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0

        rows, cols = len(matrix), len(matrix[0])
        max_area = 0
        dp = [0] * cols

        for row in range(rows):
            stack = []
            for col in range(cols + 1):
                if col < cols:
                    dp[col] = dp[col] + 1 if matrix[row][col] == '1' else 0
                while stack and (col == cols or dp[stack[-1]] >= dp[col]):
                    height = dp[stack.pop()]
                    width = col if not stack else col - stack[-1] - 1
                    max_area = max(max_area, height * width)
                stack.append(col)

        return max_area