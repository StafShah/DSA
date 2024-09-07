class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        visited = set()
        res = 0
        minH = [(0, (points[0][0], points[0][1]))]

        while len(visited) < len(points):
            dist, coordinates = heapq.heappop(minH)
            if coordinates in visited:
                continue
            visited.add(coordinates)
            res += dist

            for x, y in points:
                if (x, y) not in visited:
                    newDist = abs(coordinates[0] - x) + abs(coordinates[1] - y)
                    heapq.heappush(minH, (newDist, (x, y)))
        
        return res