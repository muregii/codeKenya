class Solution(object):
    def minIncrementForUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Sort the array to make it easier to ensure uniqueness
        nums.sort()
        
        moves = 0
        for i in range(1, len(nums)):
            # If the current number is not greater than the previous one, increment it
            if nums[i] <= nums[i - 1]:
                increment = nums[i - 1] - nums[i] + 1
                nums[i] += increment
                moves += increment
                
        return moves