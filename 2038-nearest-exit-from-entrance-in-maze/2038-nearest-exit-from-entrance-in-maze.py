class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        visited = set()
        q = collections.deque()
        q.append((0, entrance[0], entrance[1]))

        while q:
            dist, i, j = q.popleft()
            if (i, j) in visited:
                continue
            visited.add((i, j))

            if (i == 0 or i == len(maze) - 1 or j == 0 or j == len(maze[0]) - 1) and [i, j] != entrance:
                return dist
            
            directions = [[1,0],[-1,0],[0,1],[0,-1]]

            for x, y in directions:
                newR, newC = i + x, j + y
                if 0 <= newR < len(maze) and 0 <= newC < len(maze[0]) and maze[newR][newC] != '+' and (newR, newC) not in visited:
                    q.append((dist + 1, newR, newC))

        return -1        