class Solution(object):
    def sortJumbled(self, mapping, nums):
        """
        :type mapping: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        def convert(num):
            mapped_str = ''.join(str(mapping[int(digit)]) for digit in str(num))
            return int(mapped_str)
        
        return sorted(nums, key=lambda x: convert(x))