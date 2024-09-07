class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 1, len(numbers) 

        while l < r:
            if numbers[l-1] + numbers[r-1] == target:
                return l, r
            elif numbers[l-1] + numbers[r-1] > target:
                r -= 1
            else:
                l += 1
        
        return l, r