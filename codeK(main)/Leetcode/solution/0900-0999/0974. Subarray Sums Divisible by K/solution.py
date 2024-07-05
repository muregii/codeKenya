class Solution(object):
    def subarraysDivByK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        remainder_count = {0: 1}  # Start with 0 remainder count as 1 for subarrays starting from index 0
        current_sum = 0
        count = 0

        for num in nums:
            current_sum += num
            remainder = current_sum % k
            if remainder < 0:  # Handle negative remainders
                remainder += k
            
            if remainder in remainder_count:
                count += remainder_count[remainder]
                remainder_count[remainder] += 1
            else:
                remainder_count[remainder] = 1

        return count