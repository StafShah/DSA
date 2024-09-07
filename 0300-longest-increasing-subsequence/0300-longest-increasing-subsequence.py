class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        res = 1

        for i in range(len(nums) - 1, -1, -1):
            if i == len(nums) - 1:
                continue
            
            j = i
            while j < len(nums):
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
                    res = max(res, dp[i])
                j += 1
            
            # if j < len(nums):
            #     dp[i] += dp[j]
            #     res = max(res, dp[i])
            #     dp[i] = max(dp[i], dp[i + 1])
        
        return res