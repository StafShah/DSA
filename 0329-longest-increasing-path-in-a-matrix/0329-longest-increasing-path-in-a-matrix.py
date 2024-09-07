class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        dp = [[1 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        res, maxL = 0, (len(matrix) * len(matrix[0]))
        visited = set()
       
        def dfs(curr, i, j, prev):
            print(i, j)
            if prev != (-1, -1):
                dp[prev[0]][prev[1]] = max(curr + dp[i][j], dp[prev[0]][prev[1]])

            if (i, j) in visited:
                return curr + dp[i][j]
            
            visited.add((i, j))

            directions = [[1,0],[-1,0],[0,1],[0,-1]]
            for r, c in directions:
                newI, newJ = i + r, j + c
                if 0 <= newI < len(matrix) and 0 <= newJ < len(matrix[0]) and matrix[i][j] < matrix[newI][newJ] and (newI, newJ) != prev:
                    dfs(curr, newI, newJ, (i, j))
                    dp[i][j] = max(dp[i][j], 1 + dp[newI][newJ])
            
            return curr
            
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                dfs(1, i, j, (-1, -1))
                res = max(dp[i][j], res)
                if res == maxL:
                    return res
        
        print(dp)
        return res