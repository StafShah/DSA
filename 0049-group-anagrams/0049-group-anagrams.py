class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map1 = defaultdict(list)

        for gram in strs:
            hashVal = [0] * 26
            for char in gram:
                hashVal[ord(char) - ord('a')] += 1
            
            map1[tuple(hashVal)].append(gram)
        
        return map1.values()
