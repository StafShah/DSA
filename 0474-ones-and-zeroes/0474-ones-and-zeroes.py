class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = {}

        def dfs(i, totalM, totalN):
            if i == len(strs):
                return 0
            if (i, totalM, totalN) in dp:
                return dp[(i, totalM, totalN)]
            
            newM, newN = totalM, totalN
            
            for char in strs[i]:
                if char == '0':
                    newM += 1
                else:
                    newN += 1
            
            skip = dfs(i + 1, totalM, totalN)
            if newM <= m and newN <= n:
                include = 1 + dfs(i + 1, newM, newN)
            else:
                include = 0

            dp[(i, totalM, totalN)] = max(include, skip)
            return dp[(i, totalM, totalN)]
        
        return dfs(0, 0, 0)
