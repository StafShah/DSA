class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p, s = [], []
        res = []
        prefix, suffix = 1, 1
        j = len(nums) - 1

        for i in range(len(nums)):
            prefix = prefix * nums[i]
            suffix = suffix * nums[j]
            p.append(prefix)
            s.insert(0, suffix)
            j -= 1
        
        for i in range(len(nums)):
            if i == 0:
                res.append(s[i + 1])
            elif i == len(nums) - 1:
                res.append(p[i - 1])
            else:
                res.append(p[i - 1] * s[i + 1])
        
        return res