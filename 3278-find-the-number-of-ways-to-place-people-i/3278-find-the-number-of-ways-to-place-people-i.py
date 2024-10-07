class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x:(x[0],-x[1]), reverse=True)
        n = len(points)
        tot = 0

        # print(points)

        for i in range(n):
            x, y = points[i][0], points[i][1]
            highest = float('inf')

            for j in range(i + 1, n):
                if highest > points[j][1] >= y:
                    highest = points[j][1]
                    tot += 1
            
        return tot