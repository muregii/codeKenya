def maxProfit(self, prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    for i in range(len(prices)-1, 0, -1):
        prices[i] = prices[i] - prices[i-1]
    prices[0] = 0

    for i in range(1, len(prices)):
        if prices[i] + prices[i-1] > 0:
            prices[i] = prices[i] + prices[i-1]
        else:
            prices[i] = 0
    
    return max(prices)
        
