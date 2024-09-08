class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        res = 0
        adj = defaultdict(list)

        for i in range(len(edges)):
            u, v = edges[i]
            adj[u].append((succProb[i], v))
            adj[v].append((succProb[i], u))

        maxH = []
        visited = set()
        heapq.heappush(maxH, (-1, start_node))

        while maxH:
            currP, node = heapq.heappop(maxH)
            print(node)
            if node == end_node:
                res = max(res, -currP)
            if node in visited:
                continue
            visited.add(node)
            for prob, edge in adj[node]:
                if edge == end_node or edge not in visited:
                    heapq.heappush(maxH, (currP * prob, edge))
        
        return res
