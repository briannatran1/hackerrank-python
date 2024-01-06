class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''req:
            - fn takes arr of ints
            - return max profit or 0
        '''
        min_price = prices[0]
        max_profit = 0

        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)

        return max_profit

# create vars for min price and max profit
# iterate through prices arr
# update min price and max profit if another is found
# return max profit  
