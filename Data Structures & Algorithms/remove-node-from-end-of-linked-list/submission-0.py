# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        if head == None:
            return None
        
        cur = head
        length = 0
        while cur:
            length += 1
            cur = cur.next
        
        if length == n:
            return head.next

        cur = head
        for i in range(length - 1 - n):
            cur = cur.next

        cur.next = cur.next.next


        return head

        ''''''