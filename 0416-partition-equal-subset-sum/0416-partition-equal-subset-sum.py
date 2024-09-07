class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False
        
        target = sum(nums) // 2
        dp = {}

        def dfs(i, total):
            if total == target:
                return True
            
            if (i, total) in dp or i >= len(nums):
                return False

            if total > target:
                dp[(i, total)] = False
                return False

            new = dfs(i + 1, total + nums[i]) or dfs(i + 1, total)        
            dp[(i, total)] = new
            return new
        
        return dfs(0, 0)

