class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        possibleTops, possibleBottoms = [0 for _ in range(7)], [0 for _ in range(7)]

        for i in range(len(tops)):
            possibleTops[tops[i]] += 1
            possibleBottoms[bottoms[i]] += 1

        target = (0, 0)
        res = 0

        for index, (top, bottom) in enumerate(zip(possibleTops, possibleBottoms)):
            tot = top + bottom
            target = max(target, (tot, index))
        
        if possibleTops[target[1]] >= possibleBottoms[target[1]]:
            for i in range(len(tops)):
                if tops[i] != target[1]:
                    if bottoms[i] != target[1]:
                        return -1
                    res += 1
        else:
            for i in range(len(bottoms)):
                if bottoms[i] != target[1]:
                    if tops[i] != target[1]:
                        return -1
                    res += 1

        return res