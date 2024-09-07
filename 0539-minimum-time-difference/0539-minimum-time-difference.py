class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        nTimes = []
        res = 1440

        for time in timePoints:
            hr, mins = time.split(':')
            nTimes.append(int(hr) * 60 + int(mins))
        
        nTimes.sort()
        i = 0

        while i < len(nTimes):
            if i == len(nTimes) - 1:
                res = min(res, 1440 + nTimes[0] - nTimes[i])
            else:
                res = min(res, nTimes[i + 1] - nTimes[i])
            i += 1

        return res