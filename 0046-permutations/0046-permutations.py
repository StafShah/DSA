class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def dfs(subset, ns):
            if len(subset) == len(nums):
                res.append(subset.copy())
                return

            for j in range(len(ns)):
                new_subset = subset + [ns[j]]
                new_ns = ns[:j] + ns[j+1:]
                dfs(new_subset, new_ns)
        
        dfs([], nums)
        return res