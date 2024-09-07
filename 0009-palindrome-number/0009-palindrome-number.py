class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False
        
        listNum = []
        num = str(x)
        i = len(num) - 1
        
        for n in num:
            listNum.append(num[i])
            i -= 1
        
        newNum = ''.join(listNum)

        print(newNum)

        if int(newNum) == x:
            return True
        return False

