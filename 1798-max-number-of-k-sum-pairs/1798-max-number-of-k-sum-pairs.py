class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        sortedNums = sorted(nums)
        i, j, ops = 0, len(nums) - 1, 0
        while i < j:
            if sortedNums[i] + sortedNums[j] == k:
                ops += 1
                i += 1
                j -= 1
            elif sortedNums[i] + sortedNums[j] < k:
                i += 1
            else:
                j -= 1
        
        return ops