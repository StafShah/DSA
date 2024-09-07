class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        dp = {}
        if len(s1) + len(s2) != len(s3):
            return False

        def dfs(i, j, k, currSub):
            res = False
            if currSub == s3:
                return True
            
            if (i, j) in dp:
                return False
            
            if i < len(s1) and s1[i] == s3[k]:
                res = dfs(i + 1, j, k + 1, currSub + s1[i])
            
            if j < len(s2) and s2[j] == s3[k]:
                res = res or dfs(i, j + 1, k + 1, currSub + s2[j])
            
            dp[(i, j)] = res
            return res
        
        return dfs(0, 0, 0, "")