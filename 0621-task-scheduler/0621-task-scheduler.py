import heapq
from collections import deque

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        time = 0

        h = []
        for count in freq.values():
            heapq.heappush(h, -count)
        
        q = deque()

        while h or q:
            time += 1

            if h:
                num = heapq.heappop(h)
                if num + 1 != 0:
                    q.append((num + 1, time + n))
            
            if q:
                if q[0][1] == time:
                    heapq.heappush(h, q.popleft()[0])
        
        return time