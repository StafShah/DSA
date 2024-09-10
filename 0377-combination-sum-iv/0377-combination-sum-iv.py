class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = {}
        res = 0

        def dfs(i, tot):
            check = 0
            if tot > target:
                return 0
                
            if (i, tot) in dp:
                return dp[(i, tot)]

            if tot == target:
                return 1
            
            for j in range(len(nums)):
                check += dfs(j, tot + nums[j])
            
            dp[(i, tot)] = check
            return dp[(i, tot)]

        for i in range(len(nums)):
            res += dfs(i, nums[i])
        
        return res