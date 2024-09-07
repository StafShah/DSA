class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        if n == 0 or s[0] == '0':
            return 0
        
        dp = [0 for _ in range(n)]
        zeroBefore = False

        for i in range(n - 1, -1, -1):
            if s[i] == '0':
                zeroBefore = True
                continue
            
            dp[i] = 1 if i == n - 1 else dp[i + 1]

            if i < n - 1 and 10 <= int(s[i:i + 2]) <= 26:
                dp[i] += dp[i + 2] if i + 2 < n else 1

        return dp[0]