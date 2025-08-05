class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def dfs(left, right):
            if left == right:
                return nums[left]
            
            mid = (left + right) // 2

      
            if nums[mid] > nums[right]:
                return dfs(mid + 1, right)
            else:
                return dfs(left, mid)

        return dfs(0, len(nums) - 1)
