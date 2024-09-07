class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        visited = set()
        minH = [(0, (points[0][0], points[0][1]))]
        res = 0

        while minH:
            dist, coordinates = heapq.heappop(minH)
            if coordinates in visited:
                continue
            visited.add(coordinates)
            res += dist

            for x, y in points:
                if (x, y) not in visited:
                    dist1 = abs(coordinates[0] - x) + abs(coordinates[1] - y)
                    heapq.heappush(minH, (dist1, (x, y)))
            
        return res
