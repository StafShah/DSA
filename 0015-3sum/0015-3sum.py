class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sNums = sorted(nums)
        result = []
        
        for i in range(0, len(nums) - 1):
            if (i > 0 and sNums[i] == sNums[i - 1]):
                continue
            elif sNums[i] > 0:
                break

            j, k = i + 1, len(nums) - 1
            while j < k:
                if sNums[i] + sNums[j] + sNums[k] > 0:
                    k -= 1
                elif sNums[i] + sNums[j] + sNums[k] < 0:
                    j += 1
                else:
                    result.append([sNums[i], sNums[j], sNums[k]])
                    j += 1
                    while sNums[j] == sNums[j - 1] and j < k:
                        j += 1

        return result
