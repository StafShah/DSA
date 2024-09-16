import collections

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        adj = {i: [] for i in range(n)}
        reverse_adj = {i: [] for i in range(n)}
        
        for u, v in connections:
            adj[u].append(v)   
            reverse_adj[v].append(u)  
            
        res = 0
        visited = set()
        q = collections.deque([0])
        
        while q:
            curr = q.popleft()
            visited.add(curr)
            
            for neighbor in adj[curr]:
                if neighbor not in visited:
                    res += 1
                    q.append(neighbor)
            
            for neighbor in reverse_adj[curr]:
                if neighbor not in visited:
                    q.append(neighbor)
        
        return res
