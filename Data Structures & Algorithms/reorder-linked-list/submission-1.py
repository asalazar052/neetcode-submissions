# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        cur = head
        length = 0
        while cur:
            length += 1
            cur = cur.next
        
        cur = head
        for i in range((length - 1) // 2):
            cur = cur.next
        
        
        l, r = None, cur
        while r:
            temp = r.next
            r.next = l
            l = r
            r = temp

        list1 = head
        list2 = l
        while list1:
            temp1 = list1.next
            temp2 = list2.next
            list1.next = list2
            list2.next = temp1
            list1 = temp1
            list2 = temp2

    '''
    [2,4,6,8,10]

    2 -> 4 -> 6 -> 8 ->

    2 -> 4 -> ...
         ^     
    8 -> 6 -> None
         ^

    2 -> 8 -> 4 -> 6

    '''