## Explanation

- We initialize ```minPrice``` with the first element of the prices array and ```maxProfit``` with 0.
- Then, we iterate through the array, updating ```minPrice``` with the minimum value between the current price and the previous ```minPrice```, and ```maxProfit``` with the maximum value between the current profit and the previous ```maxProfit```.
- At the end of the iteration, the ```maxProfit``` variable will contain the maximum profit that can be obtained by buying and selling the stock.
- This implementation has the same time complexity of ```O(n)```, where ```n``` is the length of the prices array, as we iterate through the array only once.