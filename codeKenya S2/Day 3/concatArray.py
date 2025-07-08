
from typing import List
class Solution:
    #Acceptable, but looks “C-style”. Interviewers might ask if you know the simpler idiom
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * (2*n)

        for i in range(n):
            
            ans[i] = nums[i]
            ans[i+n] = nums[i]
        return ans
    
    # Considered the “Pythonic” answer. Shows familiarity with built-ins and writing concise code.
    def getConcatenation2(self, nums: List[int]) -> List[int]:
        return nums + nums


print(Solution().getConcatenation([1,2,3,4]))


print(Solution().getConcatenation2([1,2,3,4]))