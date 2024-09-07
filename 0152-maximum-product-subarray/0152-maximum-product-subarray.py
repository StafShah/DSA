class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        dp = [(0, 0)] * len(nums)
        dp[0] = (max(nums[0], 1), min(nums[0], 1))
        res = nums[0]

        for i in range(1, len(nums)):
            dp[i] = (max(nums[i], nums[i] * dp[i - 1][0], nums[i] * dp[i - 1][1]), min(nums[i], nums[i] * dp[i - 1][0], nums[i] * dp[i - 1][1]))
            res = max(res, dp[i][0], dp[i][1])
        
        return res