# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode(0, None)
        dcur = dummy
        cur1 = list1
        cur2 = list2

        while cur1 and cur2:

            if cur1.val <= cur2.val:
                dcur.next = cur1
                cur1 = cur1.next
            else:
                dcur.next = cur2
                cur2 = cur2.next
            
            dcur = dcur.next
        
        if cur1:
            dcur.next = cur1
        if cur2:
            dcur.next = cur2
        
        return dummy.next