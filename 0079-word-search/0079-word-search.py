class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(i, j, curr, visited):
            if board[i][j] != word[len(curr)]:
                return False

            curr += board[i][j]
            visited.add((i, j))

            if curr == word:
                return True
            
            for x, y in [(1,0),(-1,0),(0,1),(0,-1)]:
                newR, newC = i + x, j + y
                if 0 <= newR < len(board) and 0 <= newC < len(board[0]) and (newR, newC) not in visited:
                    if dfs(newR, newC, curr, visited.copy()):
                        return True
            
            return False
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if dfs(i, j, '', set()):
                        return True
        
        return False