class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        arr = sorted(list(s1))

        if len(s1) > len(s2):
            return False
        
        i, j = 0, len(s1)

        while j <= len(s2):
            if sorted(list(s2[i:j])) == arr:
                return True
            i += 1
            j += 1
        
        return False