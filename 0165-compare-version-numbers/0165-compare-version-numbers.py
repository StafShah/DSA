class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        ver1, ver2 = version1.split('.'), version2.split('.')
        print(ver1, ver2)

        for i in range(min(len(ver1), len(ver2))):
            curr1, curr2 = int(ver1[i]), int(ver2[i])
            if curr1 > curr2: return 1
            elif curr1 < curr2: return -1
        
        if len(ver1) > len(ver2):
            for i in range(len(ver2), len(ver1)):
                if int(ver1[i]) > 0:
                    return 1
        elif len(ver1) < len(ver2):
            for i in range(len(ver1), len(ver2)):
                if int(ver2[i]) > 0:
                    return -1
        
        return 0
