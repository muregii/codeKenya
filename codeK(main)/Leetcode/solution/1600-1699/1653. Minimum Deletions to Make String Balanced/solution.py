class Solution(object):
    def minimumDeletions(self, s):
        """
        :type s: str
        :rtype: int
        """
        count_b = 0
        min_deletions = 0
        
        for char in s:
            if char == 'b':
                count_b += 1
            else:  # char == 'a'
                min_deletions = min(min_deletions + 1, count_b)
        
        return min_deletions