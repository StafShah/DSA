import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        minRate = 1

        while l <= r:
            mid = (l + r) // 2
            hrs = h
            print(mid)
            
            for pile in piles:
                try:
                    hrs -= math.ceil(pile / mid)
                except:
                    pass
            
            if hrs >= 0:
                minRate = mid
                r = mid - 1
            elif hrs < 0:
                l = mid + 1
        
        return minRate