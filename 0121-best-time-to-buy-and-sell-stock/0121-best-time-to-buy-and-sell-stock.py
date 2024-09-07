class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i, j = 0, 1
        profit = 0

        while j < len(prices) and i < j:
            print(prices[j] - prices[i])
            if prices[i] < prices[j]:
                profit = max(prices[j] - prices[i], profit)
            else:
                i = j
            j += 1
        
        return profit
                
            