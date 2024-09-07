class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        i, j = 0, k - 1
        sumNum = 0
        maxNum = -10000
        if k == 1:
            return max(nums)

        while j < len(nums):
            if i == 0:
                sumNum = sum(nums[i:j + 1])
            else:
                sumNum = sumNum - nums[i - 1] + nums[j]
            print(sumNum)
            maxNum = max(maxNum, sumNum / k)
            i += 1
            j += 1
        
        return maxNum