class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        s = set(suits)

        if len(s) == 1:
            return "Flush"
        
        h = [(0,0)]
        ref = defaultdict(int)
        while ranks:
            curr = ranks.pop()
            ref[curr] += 1
            heapq.heappush(h, (ref[curr], curr))
            heapq.heappop(h)
        
        m = heapq.heappop(h)
        if m[0] >= 3:
            return "Three of a Kind"
        elif m[0] > 1:
            return "Pair"
        
        return "High Card"