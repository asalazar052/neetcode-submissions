# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        if not head or not head.next:
            return

        positions = dict() # position : node
        l, r = head, head.next
        length = 0

        # Build map and Isolate nodes
        while l:
            positions[length] = l
            length += 1
            l = l.next
        
        l = head
        while r:
            l.next = None
            l = r
            r = r.next
        
        dummy = ListNode(0, None)
        cur = dummy 
        for i in range(length // 2):
            l, r = positions[i], positions[length - i - 1]
            cur.next = l
            #if i != length - i - 1:
            l.next = r
            
            
            cur = cur.next.next
        
        if length % 2 != 0:
            cur.next = positions[length // 2]

        

'''
[0, 1, 2, 3, 4, 5, 6] -> [0, 6, 1, 5, 2, 4, 3]

0 -> 2
1 -> 4
2 -> 6

dummy -> 2 -> 6
             cur
length = 3




'''