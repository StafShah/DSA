class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float('inf')] * n
        prices[src] = 0

        for i in range(k + 1):
            temp = prices.copy()
            for s, d, p in flights:
                if prices[s] != float('inf'):
                    temp[d] = min(temp[d], p + prices[s])
            prices = temp
        
        return prices[dst] if prices[dst] != float('inf') else -1