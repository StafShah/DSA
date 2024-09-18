class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        p = []

        def isP(i, j):
            while i <= j:
                if s[i] == s[j]:
                    i += 1
                    j -= 1
                else:
                    return False
            return True

        def dfs(i):
            if i >= len(s):
                res.append(p.copy())
                return
            
            for j in range(i, len(s)):
                if isP(i, j):
                    p.append(s[i:j+1])
                    dfs(j+1)
                    p.pop()
            
        dfs(0)
        return res

             