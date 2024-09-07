# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        head = None
        curr = None
        
        while len(lists) != 0:
            minNode = None
            minI = -1
            for i in range(len(lists)):
                if lists[i] is not None:
                    if minNode is None or lists[i].val < minNode.val:
                        minNode = lists[i]
                        minI = i
            
            if minNode is None:
                break
            
            if head is None:
                head = minNode
                curr = head
            else:
                curr.next = minNode
                curr = curr.next
            
            lists[minI] = lists[minI].next

            if lists[minI] is None:
                lists.pop(minI)
        
        return head