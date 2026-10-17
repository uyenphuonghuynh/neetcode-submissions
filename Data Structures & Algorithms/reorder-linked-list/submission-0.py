# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #diving the list into 2 halves
        #using 2 pointers
        s = head
        f = head.next
        #getting the mid point
        while f and f.next:
            s = s.next
            f = f.next.next
        #slow now is mid point
        second = s.next 
        s.next = None
        #reverse the second half
        curr = nxt = ListNode()
        prev = None
        curr = second
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt 
        #prev is the new head 
        
        #reorder 
        curr = prev #assigning prev to curr for better understanding , curr before this was None
        while curr:
            first = head.next
            second = curr.next

            head.next = curr
            curr.next = first

            head = first
            curr = second
            





