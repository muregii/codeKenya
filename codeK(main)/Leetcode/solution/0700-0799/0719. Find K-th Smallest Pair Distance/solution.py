class Solution(object):
    def smallestDistancePair(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        
        # Function to count how many pairs have distance less than or equal to mid
        def countPairs(mid):
            count = 0
            left = 0
            for right in range(len(nums)):
                while nums[right] - nums[left] > mid:
                    left += 1
                count += right - left
            return count
        
        low, high = 0, nums[-1] - nums[0]
        
        # Binary search for the kth smallest distance
        while low < high:
            mid = (low + high) // 2
            if countPairs(mid) >= k:
                high = mid
            else:
                low = mid + 1
                
        return low