class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phoneDict = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        res = []
        
        def check(start, substr):
            if start == len(digits):
                if len(substr) > 0:
                    res.append(substr)
                return
            
            for char in phoneDict[digits[start]]:
                substr += char
                check(start + 1, substr)
                substr = substr[:-1]
        
        check(0, "")
        
        return res

