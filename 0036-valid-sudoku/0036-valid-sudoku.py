class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        checks = {i: set() for i in range(27)}

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] != '.' and board[i][j] in checks[i]:
                    # print(i, j, boxIndex, "row", checks)
                    return False
                checks[i].add(board[i][j])

                if board[i][j] != '.' and board[i][j] in checks[j + 9] :
                    # print(i, j, boxIndex, "col", checks)
                    return False
                checks[j + 9].add(board[i][j])

                boxIndex = ((i // 3) * 3) + (j // 3)
                
                if board[i][j] != '.' and board[i][j] in checks[boxIndex + 18]:
                    # print(i, j, boxIndex, "box", checks)
                    return False
                checks[boxIndex + 18].add(board[i][j])
        
        
        return True
            