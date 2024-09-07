import math

class Solution:
    def myAtoi(self, s: str) -> int:
        int_list = []
        minus, plus = "-", "+"
        
        def CheckNextNum(self, s: str):
            if len(s) == 1 or s[1].isdigit():
                pass
            else:
                return 'break'
            
        def CheckSym(self, s: str, l: list):
            if minus or plus in l:
                return 'del'
            elif l[len(l) - 1].isdigit():
                    return 'del'
            else:
                return 'pass'
        
        for char in s:
            if char.isdigit() or char == minus or char == plus:
                if char == minus or char == plus:
                    if len(int_list) >= 1:
                        symcheck = CheckSym(self, s, int_list)
                        if symcheck == 'del':
                            break
                int_list.append(char)
                check = CheckNextNum(self, s[s.index(char):])
                if check == 'break':
                    break
            elif char.isalpha() or char == ".":
                break
            else:
                pass
        
        if len(int_list) == 0:
            return 0
        elif len(int_list) == 1 and not int_list[0].isdigit():
            return 0
        
        result = int(''.join(int_list))
        
        if result > pow(2, 31) - 1:
            return pow(2, 31) - 1
        elif result < -1 * pow(2, 31):
            return -1 * pow(2, 31)
        else:
            return result
        
