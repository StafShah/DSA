class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        res = nums[0]
        i = 1
        s = res

        while i < len(nums):
            s += nums[i]
            check = math.ceil(s / (i + 1))
            if check > res:
                res = check
            i += 1
        
        return res