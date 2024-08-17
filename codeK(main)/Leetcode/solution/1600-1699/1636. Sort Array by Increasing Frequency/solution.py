class Solution(object):
    def frequencySort(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        from collections import Counter
        count = Counter(nums)
        sorted_nums = sorted(nums, key=lambda x: (count[x], -x))
        return sorted_nums