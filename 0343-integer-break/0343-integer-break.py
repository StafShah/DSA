class Solution:
    def integerBreak(self, n: int) -> int:
        dp = {}
        dp[1] = 1

        def dfs(remaining):
            if remaining in dp:
                return dp[remaining]
            
            factor = 0
            for i in range(1, remaining):
                res = max(i * dfs(remaining - i), i * (remaining - i))
                factor = max(factor, res)
            
            dp[remaining] = factor
            return factor
        
        return dfs(n)
