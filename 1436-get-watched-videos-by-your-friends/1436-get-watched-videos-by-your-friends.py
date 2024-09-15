class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        adj = { i:[] for i in range(len(friends)) }
        d = defaultdict(int)
        h = []

        for i in range(len(friends)):
            for friend in friends[i]:
                adj[i].append(friend)
        
        visited = set()
        q = collections.deque()
        q.append((id, 0))

        while q:
            curr, lvl = q.popleft()
            if curr in visited:
                continue
            visited.add(curr)

            if lvl == level:
                for video in watchedVideos[curr]:
                    d[video] += 1
                continue
            
            for friend in adj[curr]:
                if friend not in visited:
                    q.append((friend, lvl + 1))
        
        for video in d:
            heapq.heappush(h, (d[video], video))
        
        res = []

        while h:
            res.append(heapq.heappop(h)[1])
        
        return res