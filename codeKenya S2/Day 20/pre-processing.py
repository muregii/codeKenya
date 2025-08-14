from typing import List
# nums = [3,6,2,8,1,4,1,5]
#prefix = [3,9,11,19,20,24,25,30]
class Solution:
    def sum_from(self, nums: List[int]) -> List[int]:
        prefix = [nums[0]]
        # prefix = [3, 9]
        for i in range(1, len(nums)):
            prefix.append(nums[i] + prefix[-1])
            print(f"runnin sum : {prefix}")
        return prefix
    

#input = [3,6,2,8,1,4,1,5]
#print(Solution().sum_from(input))

def check_validity(nums, sum_from_x_to_y, limit):
    prefix = [nums[0]]
        # prefix = [3, 9]
    for i in range(1, len(nums)):
        prefix.append(nums[i] + prefix[-1])
        
    ans = [] # True, False

    for x,y in sum_from_x_to_y:
        current_window = prefix[y] - prefix[x-1]
        ans.append(current_window < limit)
    return ans

nums = [3,6,2,8,1,1,1,5]
limit = 5
print(check_validity(nums, [[1,4], [4,6]], limit))

""""Priority Queues"""

    





