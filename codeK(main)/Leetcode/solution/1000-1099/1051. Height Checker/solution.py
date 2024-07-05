class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        expected = sorted(heights)
        mismatch_count = 0
        
        for i in range(len(heights)):
            if heights[i] != expected[i]:
                mismatch_count += 1
        
        return mismatch_count