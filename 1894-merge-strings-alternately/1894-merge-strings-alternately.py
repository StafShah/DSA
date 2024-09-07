class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ''
        i, j = 0, 0

        while i < len(word1) or j < len(word2):
            if i >= len(word1):
                result += word2[j]
                j += 1
            elif j >= len(word2):
                result +=  word1[i]
                i += 1
            else:
                result += word1[i]
                result += word2[j]
                i += 1
                j += 1
        
        return result