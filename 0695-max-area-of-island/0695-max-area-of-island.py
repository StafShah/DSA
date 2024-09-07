class Solution:
    def __init__(self):
        self.maxA = 0

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        if len(grid) == 0:
            return self.maxA
        
        rows, cols = len(grid), len(grid[0])
        visited = set()

        def bfs(r, c, a):
            q = collections.deque()
            visited.add((r, c))
            self.maxA = max(self.maxA, a)
            q.append((r, c))

            directions = [[1,0], [-1,0], [0,1], [0,-1]]

            while q:
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if nr in range(rows) and nc in range(cols) and grid[nr][nc] == 1 and (nr, nc) not in visited:
                        q.append((nr, nc))
                        visited.add((nr, nc))
                        a += 1
                        self.maxA = max(self.maxA, a)
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visited:
                    bfs(r, c, 1)

        return self.maxA
