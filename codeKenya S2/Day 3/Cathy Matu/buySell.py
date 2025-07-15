class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_price = float('inf')
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price  # update buying price
            else:
                profit = price - min_price  # sell at today's price
                max_profit = max(max_profit, profit)  # update profit

        return max_profit

# Example input
prices = [7, 1, 5, 3, 6, 4]
sol = Solution()
print("Maximum Profit:", sol.maxProfit(prices))