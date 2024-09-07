"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        arr = {}
        curr = head

        while curr:
            arr[curr] = Node(curr.val)
            curr = curr.next
        
        for node in arr:
            if node.next == None:
                arr[node].next = None
            else:
                arr[node].next = arr[node.next]

            if node.random == None:
                arr[node].random = None
            else:
                arr[node].random = arr[node.random]
            
        return arr[head] if head != None else None