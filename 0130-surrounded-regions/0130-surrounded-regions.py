class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        def dfs(i, j, visit):
            print(i, j)
            if i == 0 or i == len(board) - 1 or j == 0 or j == len(board[0]) - 1:
                return None
            
            directions = [[1,0],[-1,0],[0,1],[0,-1]]
            visit.add((i, j))

            for r, c in directions:
                newR, newC = i + r, j + c
                if -1 < newR < len(board) and -1 < newC < len(board[0]) and (newR, newC) not in visit and board[newR][newC] == 'O':
                    new = dfs(newR, newC, visit)
                    if new is None:
                        return None
                    visit.update(new)

            return visit
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'O':
                    s = dfs(i, j, set([]))
                    if s is not None and (-1, -1) not in s:
                        for x, y in s:
                            board[x][y] = 'X'
        
        return