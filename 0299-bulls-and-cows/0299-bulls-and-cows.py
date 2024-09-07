class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls, cows = 0, 0
        bDict, cDict = defaultdict(int), defaultdict(int)
        
        for i in range(len(secret)):
            if guess[i] == secret[i]:
                bulls += 1
            else:
                bDict[secret[i]] += 1
                cDict[guess[i]] += 1
        
        for char in cDict:
            cows += min(bDict[char], cDict[char])
        
        return f"{bulls}A{cows}B"