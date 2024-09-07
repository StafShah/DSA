class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        s = set(nums)

        for num in nums:
            if num in s:
                s.discard(num)
            else:
                return num