class Solution(object):
    def longestIdealString(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        n = len(s)
        max_len = 1
        dp = [{} for _ in range(n)]

        for i in range(n):
            char = s[i]
            dp[i][char] = 1
            for j in range(i):
                prev_char = s[j]
                diff = abs(ord(char) - ord(prev_char))
                if diff <= k:
                    if prev_char in dp[j]:
                        dp[i][char] = max(dp[i][char], dp[j][prev_char] + 1)
                    max_len = max(max_len, dp[i][char])

        return max_len