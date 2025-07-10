from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left,right = 0,1
        curr_max = 0
        while right < len(prices):
            if prices[right] > prices[left]:
                curr_max = max(curr_max,prices[right]-prices[left])
            else:
                left = right
            right+=1

        return curr_max
