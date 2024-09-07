class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sList, tList = [*s], [*t]
        return sorted(sList) == sorted(tList)