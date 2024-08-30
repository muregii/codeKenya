class Solution(object):
    def rangeSum(self, nums, n, left, right):
        """
        :type nums: List[int]
        :type n: int
        :type left: int
        :type right: int
        :rtype: int
        """
        sub_sums = []
        mod = 10**9 + 7
        
        # Generate all subarray sums
        for i in range(n):
            current_sum = 0
            for j in range(i, n):
                current_sum += nums[j]
                sub_sums.append(current_sum)
        
        # Sort the subarray sums
        sub_sums.sort()
        
        # Sum the required range
        return sum(sub_sums[left-1:right]) % mod