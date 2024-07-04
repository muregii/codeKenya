class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        # Dictionary to store the remainder and the first occurrence index
        remainder_index_map = {0: -1}
        current_sum = 0
        
        for i, num in enumerate(nums):
            current_sum += num
            remainder = current_sum % k
            
            if remainder in remainder_index_map:
                if i - remainder_index_map[remainder] > 1:
                    return True
            else:
                remainder_index_map[remainder] = i
        
        return False