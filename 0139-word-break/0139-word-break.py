class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True

        for i in range(len(s), -1, -1):
            for j in range(i):
                if dp[j]:
                    break
                if s[j:i] in wordSet:
                    dp[j] = dp[j + len(s[j:i])]
                
        
        print(dp)
        return dp[0]
