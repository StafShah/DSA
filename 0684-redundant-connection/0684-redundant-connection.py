class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        rank = [1] * (len(edges) + 1)
        parent = [n for n in range(len(edges) + 1)]

        def find(n):
            par = parent[n]
            while par != parent[par]:
                parent[par] = parent[parent[par]]
                par = parent[par]
            return par
        
        def union(n1, n2):
            par1, par2 = find(n1), find(n2)

            if par1 == par2:
                return False
            
            if rank[par1] >= rank[par2]:
                parent[par2] = par1
                rank[par1] += rank[par2]
            else:
                parent[par1] = par2
                rank[par2] += rank[par1]
            
            return True
        
        for u,v in edges:
            if not union(u, v):
                return [u, v]
