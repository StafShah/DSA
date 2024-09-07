class Solution:
    def rob(self, nums: List[int]) -> int:
        m = {}
        i = len(nums) - 1

        if i < 2:
            return max(nums)
        
        while i >= 0:
            if i > len(nums) - 3:
                m[i] = nums[i]
            elif i < len(nums) - 3:
                m[i] = nums[i] + max(m[i + 2], m[i + 3])
            else:
                m[i] = nums[i] + m[i + 2]
            i -= 1
        
        return max(m[0], m[1])