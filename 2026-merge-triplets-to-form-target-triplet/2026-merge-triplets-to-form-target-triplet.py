class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        i = 0
        hits = set()

        while i < len(triplets):
            if triplets[i][0] > target[0] or triplets[i][1] > target[1] or triplets[i][2] > target[2]:
                triplets.pop(i)
            else:
                j = 0
                while j < 3:
                    if j in hits:
                        pass
                    elif target[j] and triplets[i][j] == target[j]:
                        hits.add(j)
                    j += 1
                if len(hits) == 3:
                    return True
                i += 1
        
        return True if len(hits) == 3 else False