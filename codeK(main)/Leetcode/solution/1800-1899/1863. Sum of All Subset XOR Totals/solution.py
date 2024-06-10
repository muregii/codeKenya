class Solution(object):
    def subsetXORSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def dfs(i, current_xor):
            if i == len(nums):
                return current_xor
            # Calculate the sum of XOR totals by including and excluding the current number
            return dfs(i + 1, current_xor ^ nums[i]) + dfs(i + 1, current_xor)
        
        return dfs(0, 0)