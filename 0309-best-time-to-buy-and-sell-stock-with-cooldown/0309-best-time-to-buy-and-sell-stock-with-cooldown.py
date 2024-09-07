class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}

        def stock(i, buying):
            if i >= len(prices):
                return 0
            
            if (i, buying) in dp:
                return dp[(i, buying)]
            
            wait = stock(i + 1, buying)
            if buying:
                buy = stock(i + 1, False) - prices[i]
                profit = max(buy, wait)
            else:
                sell = stock(i + 2, True) + prices[i]
                profit = max(sell, wait)

            dp[(i, buying)] = profit
            return dp[(i, buying)]
        
        return stock(0, True)