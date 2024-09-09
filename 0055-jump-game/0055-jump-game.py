class Solution:
    def canJump(self, nums: List[int]) -> bool:
        i = len(nums) - 1
        j = i - 1

        if j < 0:
            return True

        while i >= 0:
            curr = 1
            while nums[j] < curr:
                if j <= 0:
                    return False
                curr += 1
                j -= 1
            i = j
            j = i - 1
            if j < 0:
                return True            
                