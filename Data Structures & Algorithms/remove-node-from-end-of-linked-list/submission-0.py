# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #s,f pointers 
        f = head
        s = dummy = ListNode()
        s.next = head
        dummy.next = head

        for i in range(n):
            f = f.next
        #get to n
        while f:
            s = s.next
            f = f.next
        s.next = s.next.next
        return dummy.next










        