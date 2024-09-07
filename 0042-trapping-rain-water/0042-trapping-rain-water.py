class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        maxL, maxR = height[l], height[r]
        tot = 0
        
        while l <= r:
            if height[l] < height[r]:
                tot += max(0, min(maxL, maxR) - height[l])
                l += 1
                maxL = max(maxL, height[l])
            else:
                tot += max(0, min(maxL, maxR) - height[r])
                r -= 1
                maxR = max(maxR, height[r])
        
        return tot
                