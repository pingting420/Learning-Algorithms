def maxProfit(prices):
    minprice = float('inf')
    maxprofit = 0
    for price in prices:
        minprice = (minprice, price)
        maxprofit = (maxprofit,price - minprice)
    return maxprofit
#Time complexity: O(N)
