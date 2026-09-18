# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode(0, head)
        cur = None
        cur2 = head

        while cur2:
           temp = cur2.next
           cur2.next = cur
           cur = cur2
           cur2 = temp
        
        return cur

'''
None <- 1 -> 2 -> 3 -> None
  cur   cur2
       
temp = 2

'''
