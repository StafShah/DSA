class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        currTime = 0

        visited = set()
        minH = []
        heapq.heappush(minH, (grid[0][0], 0, 0))

        while minH:
            t, r, c = heapq.heappop(minH)
            if (r, c) in visited:
                continue

            visited.add((r, c))
            currTime = max(currTime, t)
            
            if (r, c) == (len(grid) - 1, len(grid) - 1):
                return currTime

            directions = [[1,0],[-1,0],[0,1],[0,-1]]

            for x, y in directions:
                newR, newC = r + x, c + y
                if 0 <= newR < len(grid) and 0 <= newC < len(grid) and (newR, newC) not in visited:
                    heapq.heappush(minH, (grid[newR][newC], newR, newC))
            
        return currTime