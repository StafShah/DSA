import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        s = [-stone for stone in stones]
        heapq.heapify(s)

        while len(s) > 1:
            s1, s2 = heapq.heappop(s), heapq.heappop(s)
            if s2 > s1:
                heapq.heappush(s, s1 - s2)
        
        s.append(0)
        return abs(s[0])