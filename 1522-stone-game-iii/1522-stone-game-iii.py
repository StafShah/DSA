class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        dp = [0] * (len(stoneValue) + 1)
        i, n = len(stoneValue) - 1, len(stoneValue)

        while i >= 0:
            best = -float('inf')
            best = max(stoneValue[i] - dp[i + 1], best)

            if i + 1 < n:
                best = max(stoneValue[i] + stoneValue[i + 1] - dp[i + 2], best)
            
            if i + 2 < n:
                best = max(stoneValue[i] + stoneValue[i + 1] + stoneValue[i + 2] - dp[i + 3], best)
            
            dp[i] = best
            i -= 1
        
        res = dp[0]

        if res > 0:
            return "Alice"
        elif res < 0:
            return "Bob"
        else:
            return "Tie"