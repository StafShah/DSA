class Solution:
    def __init__(self):
        self.pacific = False
        self.atlantic = False
    
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        res = []

        def checkSpread(visited, i, j):
            if j == 0 or i == 0:
                self.pacific = True
            
            if i == len(heights) - 1 or j == len(heights[0]) - 1:
                self.atlantic = True

            if self.pacific and self.atlantic:
                return True

            visited.add((i, j))
            directions = [[1,0],[-1,0],[0,1],[0,-1]]
            
            for r, c in directions:
                newR, newC = i + r, j + c
                if 0 <= newR < len(heights) and 0 <= newC < len(heights[0]) and (newR, newC) not in visited and heights[newR][newC] <= heights[i][j]:
                    if checkSpread(visited, newR, newC):
                        return True
            return False

        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if checkSpread(set(), i, j):
                    res.append([i, j])
                self.atlantic, self.pacific = False, False
        
        return res
