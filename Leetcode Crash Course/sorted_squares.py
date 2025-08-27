from typing import List
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ans = []
        i, j = 0, 1
        for num in nums: # O(n)
            sq = num*num
            ans.append(sq)
        
        while i < len(ans) and j < len(ans) :
            if ans[j] < ans[i]:
                ans[i] = ans[j]
                i+=1
                j+=1
                
        return ans
        
test = [-4,0,1]
res = Solution().sortedSquares(test)
print(res)


