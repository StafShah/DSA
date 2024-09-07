class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        nums.sort() 

        def dfs(i, subset, ns):
            if i == len(ns): 
                return

            for j in range(i, len(ns)):
                if j > i and ns[j] == ns[j-1]: 
                    continue
                new_subset = subset + [ns[j]]
                res.append(new_subset)
                dfs(j + 1, new_subset, ns)

        dfs(0, [], nums)
        return res