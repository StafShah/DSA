class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        maxVals = defaultdict(int)
        res = []

        for i in range(len(s)):
            maxVals[s[i]] = i
        
        i = 0

        while i < len(s):
            start = i
            currMax = maxVals[s[i]]
            while i <= currMax:
                currMax = max(currMax, maxVals[s[i]])
                i += 1
            res.append(currMax - start + 1)

        return res