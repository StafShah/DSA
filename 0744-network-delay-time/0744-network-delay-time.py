class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        child = defaultdict(list)
        res = 0

        for u, v, t in times:
            child[u].append((t, v))

        visited = set()
        minH = [(0, k)]

        while minH:
            dist1, node = heapq.heappop(minH)
            if node in visited:
                continue
            visited.add(node)
            res = dist1

            for dist, c in child[node]:
                heapq.heappush(minH, (dist + dist1, c))
        
        return res if len(visited) == n else -1