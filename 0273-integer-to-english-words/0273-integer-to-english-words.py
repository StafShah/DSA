class Solution:
    def numberToWords(self, num: int) -> str:
        res = ""
        m = {0: ('Zero', 'Zero'), 1: ('One', 'Ten'), 2: ('Two', 'Twenty'), 3: ('Three', 'Thirty'), 4: ('Four', 'Forty'), 
            5: ('Five','Fifty'),  6: ('Six', 'Sixty'), 7: ('Seven', 'Seventy'), 8: ('Eight', 'Eighty'), 
            9: ('Nine', 'Ninety'), 10: 'Ten', 11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', 
            15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen'}
        
        num = str(num)

        if len(num) == 10:
            res += m[int(num[0])][0] + " Billion "
            num = num[1:]
        elif len(num) == 1:
            return m[int(num)][0]
        
        while len(num) > 0:
            if int(num) // 1000000 > 0:
                num = str(int(num))
                n = num[0:(len(num) - 6)]
                num = str(int(num) - (int(num) // 1000000) * 1000000)
                if len(n) == 3 and n[0] != '0':
                    res += m[int(n[0])][0] + " Hundred "
                    if n[1] != '0':
                        n = n[1:]
                    else:
                        n = n[2:]
                if len(n) == 2 and n[0] != '0':
                    if int(n) > 9 and int(n) < 20:
                        res += m[int(n)] + " "
                        n = ""
                    else:
                        res += m[int(n[0])][1] + " "
                        if n[1] != '0':
                            n = n[1:]
                        else:
                            n = ""
                if len(n) == 1 and n[0] != '0':
                    res += m[int(n[0])][0] + " "
                res += "Million "
            elif int(num) // 1000 > 0:
                num = str(int(num))
                n = num[0:len(num) - 3]
                num = str(int(num) - (int(num) // 1000) * 1000)
                if len(n) == 3 and n[0] != '0':
                    res += m[int(n[0])][0] + " Hundred "
                    if n[1] != '0':
                            n = n[1:]
                    else:
                        n = n[2:]
                if len(n) == 2 and n[0] != '0':
                    if int(n) > 9 and int(n) < 20:
                        res += m[int(n)] + " "
                        n = ""
                    else:
                        res += m[int(n[0])][1] + " "
                        if n[1] != '0':
                            n = n[1:]
                        else:
                            n = ""
                if len(n) == 1 and n[0] != '0':
                    res += m[int(n[0])][0] + " "
                res += "Thousand "
            else:
                num = str(int(num))
                if len(num) == 3 and num[0] != '0':
                    res += m[int(num[0])][0] + " Hundred "
                    if num[1] != '0':
                        num = num[1:]
                    else:
                        num = num[2:]
                if len(num) == 2 and num[0] != '0':
                    if int(num) > 9 and int(num) < 20:
                        res += m[int(num)] + " "
                        num = ""
                    else:
                        res += m[int(num[0])][1] + " "
                        if num[1] != '0':
                            num = num[1:]
                        else:
                            num = ""
                if len(num) == 1 and num[0] != '0':
                    res += m[int(num[0])][0] + " "
                num = ""
            
        return res[:-1]