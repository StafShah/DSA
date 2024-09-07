from collections import defaultdict, deque

class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        ancestors = [set() for _ in range(n)]
        graph = defaultdict(list)
        in_degree = [0] * n
        
        for u, v in edges:
            graph[u].append(v)
            in_degree[v] += 1
        
        q = deque([i for i in range(n) if in_degree[i] == 0])
        
        while q:
            node = q.popleft()
            for child in graph[node]:
                ancestors[child].update(ancestors[node])
                ancestors[child].add(node)
                in_degree[child] -= 1
                if in_degree[child] == 0:
                    q.append(child)
        
        return [sorted(list(ancestor_set)) for ancestor_set in ancestors]