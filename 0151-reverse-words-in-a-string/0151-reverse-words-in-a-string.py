class Solution:
    def reverseWords(self, s: str) -> str:
        chars, words = [], []
        i = len(s) - 1
        while i > -1:
            while i > -1 and s[i] != ' ':
                chars.append(s[i])
                print(i)
                i -= 1
            if (i <= -1 or s[i] == ' ') and len(chars) > 0:
                print(chars)
                words.append(''.join(chars[::-1]))
                chars = []
            print(i)
            i -= 1
        
        return ' '.join(words)