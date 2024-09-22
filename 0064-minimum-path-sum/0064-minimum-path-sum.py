class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp = [[float('inf') for _ in range(len(grid[0]) + 1)] for _ in range(len(grid) + 1)]
        dp[-2][-2] = grid[-1][-1]

        for i in range(len(grid) - 1, -1, -1):
            for j in range(len(grid[0]) - 1, -1, -1):
                if dp[i][j] != float('inf'):
                    continue
                dp[i][j] = grid[i][j] + min(dp[i][j+1], dp[i+1][j])
        
        return dp[0][0]