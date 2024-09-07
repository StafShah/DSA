class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for num in nums:
            if num - 1 not in numSet:
                temp = num + 1
                while temp in numSet:
                    temp += 1
                longest = max(longest, temp - num)
        
        return longest
            
