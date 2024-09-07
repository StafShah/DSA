class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        subset = []

        def dfs(start, target):
            if target == 0:
                res.append(subset.copy())
                return
            elif target < 0:
                return

            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                subset.append(candidates[i])
                dfs(i + 1, target - candidates[i])
                subset.pop()
                

        dfs(0, target)             

        return res