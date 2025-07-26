from typing import List
class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(start, path, total):
            # Base case: found a valid combination
            if total == target:
                res.append(path[:])
                return
            # Base case: exceeded target
            if total > target:
                return

            # Explore from current index onwards to allow repeated usage
            for i in range(start, len(nums)):
                path.append(nums[i])                 # Choose nums[i]
                backtrack(i, path, total + nums[i])  # Not i+1 because we can reuse the same element
                path.pop()                           # Backtrack

        backtrack(0, [], 0)
        return res
