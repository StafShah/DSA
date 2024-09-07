class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        sNums = sorted(nums)
        i = 0
        pNum = 0

        while i < len(nums):
            if sNums[i] > 0:
                if sNums[i] - pNum > 1:
                    print(pNum)
                    return pNum + 1;
                if sNums[i] != pNum:
                    pNum += 1
            i += 1
        
        return sNums[-1] + 1 if sNums[-1] > 0 else 1

