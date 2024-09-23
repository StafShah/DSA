class Solution:
    def integerReplacement(self, n: int) -> int:
        dp = {}

        def dfs(i):
            if i in dp:
                return dp[i]
            if i == 1:
                return 1

            if i % 2 == 0:
                dp[i] = 1 + dfs(i / 2)
            else:
                dp[i] = 1 + min(dfs(i + 1), dfs(i - 1))
            
            return dp[i]
        
        return dfs(n) - 1