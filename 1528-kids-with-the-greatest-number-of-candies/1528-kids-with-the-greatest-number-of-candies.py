class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result = []
        highestCandies = max(candies)
        for kid in candies:
            if highestCandies <= (kid + extraCandies):
                result.append(True)
            else:
                result.append(False)
        
        return result