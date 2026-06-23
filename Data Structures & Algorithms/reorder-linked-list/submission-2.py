# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        s, f = head, head

        # Get to the halfway point of the list
        while f and f.next: # Check condition
            s = s.next
            f = f.next.next
        
        l = None
        r = s

        # Reverse second half
        while r:
            temp = r.next
            r.next = l
            l = r
            r = temp

        first = head
        second = l

        while second.next:
            t1 = first.next
            t2 = second.next

            first.next = second
            second.next = t1

            first = t1
            second = t2
  
'''
2 -> 4
8 -> 6

2 -> 4 -> 8 -> 
'''
        

        
