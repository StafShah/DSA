class Solution:
    def minWindow(self, s: str, t: str) -> str:
        curr = {}
        res = None
        i, j = 0, 0

        for char in t:
            if char not in curr:
                curr[char] = [0, 1]
            else:
                curr[char][1] += 1

        while j < len(s):
            if s[j] in curr:
                curr[s[j]][0] += 1
                valid = True
                for state, tot in curr.values():
                    if state < tot:
                        valid = False
                        break
                if valid:
                    if not res or len(s[i:j + 1]) < len(res):
                        res = s[i:j + 1]

                if valid and curr[s[j]][0] >= curr[s[j]][1]:
                    while True:
                        if s[i] in curr:
                            if curr[s[i]][0] > curr[s[i]][1]:
                                curr[s[i]][0] -= 1
                            else:
                                break
                        i += 1
                        
                        if len(s[i:j + 1]) < len(res):
                            res = s[i:j + 1]
            j += 1
        
        return res if res else ""
            