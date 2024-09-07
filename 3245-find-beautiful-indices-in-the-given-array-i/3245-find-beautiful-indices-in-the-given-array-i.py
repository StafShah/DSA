class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        res = []
        m = {'a': [], 'b': []}
        i = 0

        while i < len(s):
            nextAdv = []
            if s[i] == a[0]:
                currS = s[i]
                if len(a) > 1:
                    j = i
                    j += 1
                    while len(currS) < len(a) and j < len(s):
                        currS += s[j]
                        if currS != a[:len(currS)]:
                            break
                        j += 1
                if currS == a:
                    m['a'].append(i)
                    nextAdv.append(len(a))
            
            if s[i] == b[0]:
                currS = s[i]
                if len(b) > 1:
                    j = i
                    j += 1
                    while len(currS) < len(b) and j < len(s):
                        currS += s[j]
                        if currS != b[:len(currS)]:
                            break
                        j += 1
                if currS == b:
                    m['b'].append(i)
                    nextAdv.append(len(b))
            
            # if len(nextAdv) > 1:
            #     i += min(nextAdv)
            #     continue
            
            i += 1
        
        for idxA in m['a']:
            for idxB in m['b']:
                if abs(idxA - idxB) <= k:
                    res.append(idxA)
                    break
        
        return sorted(res)