"""
nums = [1 2 3]
curr = [1,2,3]
ans =[[1,2,3]]
[]
123
132
213
231
321
312

Example 1: 46. Permutations

Given an array nums of distinct integers, return all the possible permutations in any order.

For example, given nums = [1, 2, 3], return [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]].
"""
from typing import List
class Solution:
    def permutation(self, nums: List[int]) -> List[List[int]]:
        def backtrack(curr): 
            #base case
            if len(curr) == len(nums):
                ans.append(curr[:]) 
                return 
            
            for num in nums: 
                if num not in curr:
                    curr.append(num)
                    backtrack(curr)
                    curr.pop()

            
        ans = []
        backtrack([])
        return ans

test = [1,2,3]
res = Solution().permutation(test)
print(res)


#curr = [1, 2, 3]
#backtrack(curr=1)

#backtrack(curr= 1, 2)
#loop 
#backtrack(curr= 1, 2, 3)

# ans = [[1,2,3]]

#curr.pop() = [1,2,<-]
# curr =[1]

#backtrack([curr= 1, 3, 2])

# ans = [[1,2,3] [1,3,2] ,[2,1,3]]

#curr = [1,3]

#Call Stack                            curr               Action
#--------------------------------------------------------------------
#backtrack([])                         []                 start
#
#└─ Try num=1                          [1]                curr.append(1)
#   └─ backtrack([1])                  [1]                recurse
#
#      ├─ Try num=1                    [1]                skipped (already in curr)
#      ├─ Try num=2                    [1,2]              curr.append(2)
#      │  └─ backtrack([1,2])          [1,2]              recurse
#
#      │     ├─ Try num=1              [1,2]              skipped
#      │     ├─ Try num=2              [1,2]              skipped
#      │     └─ Try num=3              [1,2,3]            curr.append(3)
#      │        └─ backtrack([1,2,3])  [1,2,3]            recurse
#
#      │           → len(curr)==3 →     [1,2,3]            ans.append([1,2,3])
#      │           ← return             [1,2,3]
#      │     ← pop()                    [1,2]              undo choice 3
#
#      │  ← pop()                       [1]                undo choice 2
#      │
#      └─ Try num=3                     [1,3]              curr.append(3)
#         └─ backtrack([1,3])           [1,3]              recurse
#
#            ├─ Try num=1               [1,3]              skipped
#            ├─ Try num=2               [1,3,2]           curr.append(2)
#            │  └─ backtrack([1,3,2])   [1,3,2]           recurse
#
#            │     → len(curr)==3 →      [1,3,2]           ans.append([1,3,2])
#            │  ← pop()                  [1,3]             undo choice 2
#
#            └─ Try num=3               [1,3]             skipped
#         ← pop()                       [1]                undo choice 3
#
#   ← pop()                             []                 undo choice 1
#
#└─ Try num=2                          [2]                curr.append(2)
#   └─ backtrack([2])                  [2]
#
#      ├─ Try num=1                    [2,1]             curr.append(1)
#      │  └─ backtrack([2,1])          [2,1]
#
#      │     └─ Try num=3              [2,1,3]          curr.append(3)
#      │        └─ backtrack([2,1,3])  [2,1,3]
#      │           → append([2,1,3])
#      │        ← pop()                 [2,1]            undo 3
#      │     ← pop()                   [2]               undo 1
#
#      └─ Try num=2                    [2]               skipped
#      └─ Try num=3                    [2,3]             curr.append(3)
#         └─ backtrack([2,3])          [2,3]
#
#            └─ Try num=1              [2,3,1]          curr.append(1)
#               └─ backtrack([2,3,1])  [2,3,1]
#                  → append([2,3,1])
#               ← pop()                 [2,3]           undo 1
#            ← pop()                   [2]              undo 3
#
#   ← pop()                             []                undo 2
#
#└─ Try num=3                          [3]               curr.append(3)
#   └─ backtrack([3])                  [3]
#
#      ├─ Try num=1                    [3,1]            curr.append(1)
#      │  └─ backtrack([3,1])          [3,1]
#
#      │     └─ Try num=2              [3,1,2]          curr.append(2)
#      │        → append([3,1,2])
#      │     ← pop()                   [3,1]            undo 2
#      │  ← pop()                      [3]              undo 1
#
#      └─ Try num=2                    [3,2]            curr.append(2)
#         └─ backtrack([3,2])          [3,2]
#
#            └─ Try num=1              [3,2,1]          curr.append(1)
#               → append([3,2,1])
#            ← pop()                   [3,2]           undo 1
#         ← pop()                       [3]              undo 2
#
#   ← pop()                             []                undo 3
#
#(backtrack([]) ends)
#