class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []

        def dfs(i):
            s = sum(subset)
            if s > target:
                return
            elif i >= len(candidates):
                if s == target:
                    res.append(subset.copy())
                return
            elif s == target:
                res.append(subset.copy())
                return
            
            subset.append(candidates[i])
            dfs(i)

            subset.pop()
            dfs(i + 1)
        
        dfs(0)
        return res
            
