class Solution:
    def jump(self, nums: List[int]) -> int:
        i = len(nums) - 1
        jumps = 0

        while i > 0:
            nextI = i
            for j in range(0, i):
                if j + nums[j] >= i:
                    nextI = j
                    break
            jumps += 1
            i = j
        
        return jumps
                