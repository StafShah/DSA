# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        str1, str2 = '', ''
        head1, head2 = l1, l2
        result = ListNode()

        while head1 or head2:
            if head1:
                str1 = str(head1.val) + str1
                head1 = head1.next
            
            if head2:
                str2 = str(head2.val) + str2
                head2 = head2.next
        
        res = str(int(str1) + int(str2))
        prev = None

        for i in range(len(res)):
            result.val = int(res[i])
            result.next = prev
            newN = ListNode(None, result)
            prev = result
            result = newN
        
        return prev