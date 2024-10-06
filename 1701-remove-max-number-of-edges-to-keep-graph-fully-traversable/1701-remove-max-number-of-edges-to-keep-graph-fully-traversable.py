class UF:
    def __init__(self, n):
        self.n = n
        self.parent = [i for i in range(n + 1)]
        self.rank = [1 for _ in range(n + 1)]
    
    def find(self, node):
        while self.parent[node] != node:
            node = self.parent[node]
        return node
    
    def union(self, node1, node2):
        par1, par2 = self.find(node1), self.find(node2)
        if par1 == par2:
            return 0
        
        if self.rank[par1] >= self.rank[par2]:
            self.parent[par2] = par1
            self.rank[par1] += par2
        else:
            self.parent[par1] = par2
            self.rank[par2] += par1

        self.n -= 1
        return 1

    def isConnected(self):
        return self.n == 1

class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        alice, bob = UF(n), UF(n)
        count = 0

        for t, u, v in edges:
            if t == 3:
                count += (alice.union(u, v) | bob.union(u, v))
        
        for t, u, v in edges:
            if t == 2:
                count += bob.union(u, v)
            elif t == 1:
                count += alice.union(u, v)
        
        if alice.isConnected() and bob.isConnected():
            return len(edges) - count
        return -1