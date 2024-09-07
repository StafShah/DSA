class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        currMin, currMax = -1, -1
        i = 0

        while i < len(intervals) - 1:
            currMin, currMax = intervals[i + 1][0], intervals[i][1]
            if currMax >= currMin:
                newMin, newMax = min(intervals[i+1][0], intervals[i][0]), max(intervals[i][1], intervals[i + 1][1])
                intervals[i] = [newMin, newMax]
                intervals.pop(i + 1)
            else:
                i += 1
        
        return intervals