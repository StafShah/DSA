class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        dp = {}
        res = 0

        for i in range(len(questions) - 1, -1, -1):
            m = questions[i][0]
            if (i + questions[i][1] + 1) < len(questions):
                j = (i + questions[i][1] + 1)
                m += dp[j]

            if i + 1 < len(questions):
                m = max(m, dp[i + 1])
            
            dp[i] = m
            res = max(res, dp[i])
        
        return res
