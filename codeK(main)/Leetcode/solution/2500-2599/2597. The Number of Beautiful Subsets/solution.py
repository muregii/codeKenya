class Solution(object):
    def beautifulSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def is_beautiful(subset):
            for i in range(len(subset)):
                for j in range(i + 1, len(subset)):
                    if abs(subset[i] - subset[j]) == k:
                        return False
            return True
        
        def dfs(index, path):
            if path and is_beautiful(path):
                result.append(path)
            for i in range(index, len(nums)):
                dfs(i + 1, path + [nums[i]])
        
        result = []
        dfs(0, [])
        return len(result)
