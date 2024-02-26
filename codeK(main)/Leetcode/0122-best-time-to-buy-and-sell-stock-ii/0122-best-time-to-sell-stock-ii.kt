class Solution {
    fun maxProfit(prices: IntArray): Int {

        if (prices.size < 2) return 0

        var maxProfit = 0
        var minPrice = prices[0]

        for (i in 0 until prices.size) {
            minPrice = minOf(minPrice, prices[i])
            maxProfit = maxOf(maxProfit, prices[i] - minPrice)

        }
        return maxProfit
    }
}