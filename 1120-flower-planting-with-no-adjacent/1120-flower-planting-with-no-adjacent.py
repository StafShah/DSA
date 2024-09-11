class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        adj = { i:[] for i in range(n + 1)}
        types = [0 for _ in range(n + 1)]

        for g1, g2 in paths:
            adj[g1].append(g2)
            adj[g2].append(g1)

        q = collections.deque()
        visited = set()

        for i in range(n + 1):
            if i in visited:
                continue
            types[i] = 1
            q.append(i)
            while q:
                curr = q.popleft()
                if curr in visited:
                    continue
                visited.add(curr)
                j = 1

                for path in adj[curr]:
                    typeSet = set([types[neighbor] for neighbor in adj[path]])
                    if path not in visited:
                        while j > 4 or j == types[curr] or j in typeSet:
                            if j >= 4: j = 1
                            else: j += 1
                        q.append(path)
                        # if types[path] == 0 or types[path] == types[curr]:
                        types[path] = j
                        j += 1
        
        return types[1:]
