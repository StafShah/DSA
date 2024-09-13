class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        adj = { i:[] for i in range(len(isConnected))}
        res = 0

        for i in range(len(isConnected)):
            for j in range(len(isConnected)):
                if isConnected[i][j]:
                    adj[i].append(j)
        
        visited = set()

        def dfs(i):
            if i in visited:
                return
            
            visited.add(i)

            for j in adj[i]:
                if j not in visited:
                    dfs(j)
            
        for i in range(len(isConnected)):
            if i in visited:
                continue
            
            dfs(i)
            res += 1
        
        return res