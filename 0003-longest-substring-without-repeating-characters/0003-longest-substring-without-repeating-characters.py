class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i, j = 0, 1
        maxLen = 1
        d = defaultdict(lambda: 0)

        if len(s) == 0:
            return 0
        
        d[s[i]] += 1

        while j < len(s):
            d[s[j]] += 1

            while not set(d.values()).issubset({0, 1}):
                d[s[i]] -= 1
                i += 1

            maxLen = max(len(s[i:j+1]), maxLen)
            j += 1
        
        return maxLen
