class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        w, l, ls = {}, {}, {}

        for match in matches:
            if match[0] not in w and match[0] not in l and match[0] not in ls:
                w[match[0]] = True
            
            if match[1] in w and match[1] not in l:
                l[match[1]] = True
                w.pop(match[1])
            elif match[1] in l and match[1] not in ls:
                l.pop(match[1])
                ls[match[1]] = True
            elif match[1] in ls:
                pass
            else:
                l[match[1]] = True
                    
        return [sorted(w.keys()), sorted(l.keys())]