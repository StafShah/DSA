class Solution:
    def numSquares(self, n: int) -> int:
        dp = {}
        
        def dfs(curr):
            if curr in dp:
                return dp[curr]
            
            if curr == 0:
                return 0 
            
            min_squares = float('inf')
            
            i = 1
            while i * i <= curr:
                min_squares = min(min_squares, 1 + dfs(curr - i * i))
                i += 1
            
            dp[curr] = min_squares
            return dp[curr]
        
        return dfs(n)
