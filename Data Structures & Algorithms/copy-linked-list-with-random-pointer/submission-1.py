"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return
        
        cpy = {}
        # dummy = Node(0, head, None)
        cur = head

        while cur:
            cpy[cur] = Node(cur.val, None, None) # creates a copy of each node
            cur = cur.next
        
        cur = head
        while cur:
            if cur.next:
                cpy[cur].next = cpy[cur.next]

            if cur.random:
                cpy[cur].random = cpy[cur.random]
            
            cur = cur.next
        
        print(cpy)

        return cpy[head]
        


        
