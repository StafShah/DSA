class Solution:
    def romanToInt(self, s: str) -> int:
        result, idx = 0, 0
        resultDict = {'M': 1000, 'CM': 900, 'D': 500, 'CD': 400, 'C': 100, 'XC': 90, 'L': 50, 'XL': 40, 'X': 10, 'IX': 9, 'V': 5, 'IV': 4, 'I': 1}
        
        while idx <= len(s) - 1:
            if idx < len(s) - 1: 
                if s[idx] + s[idx + 1] in resultDict:
                    result += resultDict[s[idx] + s[idx + 1]]
                    idx += 2
                    continue
            result += resultDict[s[idx]]
            idx += 1
        
        return result

