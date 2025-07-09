#Assignment 3: Best Time to Buy and Sell Stock Leet Code Challenge
#You are given an array prices where prices[i] is the price of a given stock on the ith day.
#You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
#Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
#Assumption: Buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

def maxProfit(prices):
    buy_price = float('inf')  
    best_profit = 0           

    for price in prices:
        if price < buy_price:
            
            buy_price = price
        else:
           
            profit = price - buy_price
            if profit > best_profit:
                best_profit = profit

    return best_profit

# Example usage:
if __name__ == "__main__":
    prices = [7, 1, 5, 3, 6, 4]
    print("Stock prices:", prices)
    print("Maximum profit:", maxProfit(prices)) 


