class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        m = {}

        for domain in cpdomains:
            num, domain = domain.split(' ')
            d = domain.split('.')
            while len(d) > 0:
                if len(d) == 1:
                    if d[0] in m:
                        m[d[0]] += int(num)
                    else:
                        m[d[0]] = int(num)
                    d.pop()
                else:
                    s = '.'.join(d)
                    if s in m:
                        m[s] += int(num)
                    else:
                        m[s] = int(num)
                    d.pop(0)
        
        return [str(value) + ' ' + key for key, value in m.items()]