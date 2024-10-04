class Solution:
    def maxNumOfMarkedIndices(self, nums: List[int]) -> int:
        smallH = []
        res = 0
        nums.sort()

        for i in range(len(nums) // 2):
            heapq.heappush(smallH, -nums[i])
        
        currLarge = -1
        while smallH:
            check = heapq.heappop(smallH)
            if -check * 2 <= nums[currLarge]:
                res += 2
                currLarge -= 1
        
        return res