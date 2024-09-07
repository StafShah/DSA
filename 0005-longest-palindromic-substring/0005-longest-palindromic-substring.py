class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""

        def checkPalindrome(i):
            odd, even = s[i], ""
            j, k = i - 1, i + 1
            while (j >= 0 and k < len(s)):
                if s[j] == s[k]:
                    odd = s[j] + odd + s[k]
                    j -= 1
                    k += 1
                else:
                    break
            
            l, m = i, i + 1
            while (l >= 0 and m < len(s)):
                if s[l] == s[m]:
                    even = s[l] + even + s[m]
                    l -= 1
                    m += 1
                else:
                    break
            
            if len(odd) > len(even):
                return odd
            else:
                return even
        
        for i in range(len(s)):
            new = checkPalindrome(i)
            if len(new) > len(res):
                res = new
        
        return res