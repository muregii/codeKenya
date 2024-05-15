class Solution(object):
    def findMaxK(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_set = set(nums)
        max_k = -1
        for num in nums:
            if -num in num_set and num > max_k:
                max_k = num
        return max_k