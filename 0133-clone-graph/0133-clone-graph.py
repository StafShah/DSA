"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node == None:
            return None
        
        newNode = Node(node.val, None)
        newMap = {1: newNode}

        if node.neighbors == []:
            return newNode

        visited = set()
        q = collections.deque()
        q.append(node)

        while q:
            curr = q.popleft()
            visited.add(curr.val)
            for neighbor in curr.neighbors:
                if neighbor.val not in newMap:
                    rep = Node(neighbor.val, None)
                    newMap[curr.val].neighbors.append(rep)
                    newMap[neighbor.val] = rep
                else:
                    newMap[curr.val].neighbors.append(newMap[neighbor.val])
                
                if neighbor.val not in visited and neighbor not in q:
                    q.append(neighbor)
        
        return newNode