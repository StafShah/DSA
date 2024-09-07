import collections

class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        adj = {i: [] for i in range(1, n + 1)}
        
        for person, disliked in dislikes:
            adj[person].append(disliked)
            adj[disliked].append(person)
        
        color = {}
        
        def bfs(start):
            q = collections.deque([start])
            color[start] = 0 
            
            while q:
                node = q.popleft()
                
                for neighbor in adj[node]:
                    if neighbor not in color:
                        color[neighbor] = 1 - color[node] 
                        q.append(neighbor)
                    elif color[neighbor] == color[node]:
                        return False 
                    
            return True
        
        for i in range(1, n + 1):
            if i not in color:
                if not bfs(i):
                    return False
        
        return True
