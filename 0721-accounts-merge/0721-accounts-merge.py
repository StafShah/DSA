from collections import defaultdict, deque
from typing import List

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        adj = defaultdict(set)
        res = []

        for account in accounts:
            first_email = account[1]
            for i in range(1, len(account)):
                adj[account[i]].add(first_email)
                adj[first_email].add(account[i])
                for j in range(i + 1, len(account)):
                    adj[account[i]].add(account[j])
                    adj[account[j]].add(account[i])
        
        visited = set()

        for account in accounts:
            name = account[0]
            first_email = account[1]

            if first_email not in visited:
                profile = [name]
                q = deque([first_email])

                while q:
                    curr = q.popleft()
                    if curr not in visited:
                        visited.add(curr)
                        profile.append(curr)
                        for neighbor in adj[curr]:
                            if neighbor not in visited:
                                q.append(neighbor)
                
                res.append([profile[0]] + sorted(profile[1:]))

        return res
