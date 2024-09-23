class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        initial = 0
        total = 0
        ref = len(nums)

        for i in range(len(nums)):
            initial += (nums[i] * i)
            total += nums[i]

        res = initial
        i = ref - 1

        while i > 0:
            initial += total - (nums[i] * ref)
            res = max(res, initial)
            i -= 1
        
        return res