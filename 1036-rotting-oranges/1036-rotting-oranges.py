class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        count = {1: 0}
        rottens, tempq = collections.deque(), collections.deque()
        mins = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    count[1] += 1
                elif grid[i][j] == 2:
                    rottens.append((i, j))
        
        if len(rottens) == 0 and count[1] != 0: return -1

        while count[1] > 0:
            x, y = rottens.popleft()

            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

            for r, c in directions:
                nr, nc = x+r, y+c
                if (nr >= 0 and nr < len(grid)) and (nc >= 0 and nc < len(grid[0])) and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    count[1] -= 1
                    tempq.append((nr, nc))
            
            print(grid)
            print(" ")

            if count[1] == 0:
                mins += 1
                break

            if len(rottens) == 0:
                print("true")
                if len(tempq) == 0 and count[1] > 0:
                    return -1
                mins += 1
                rottens = tempq.copy()
                tempq.clear()
                
        return mins
            