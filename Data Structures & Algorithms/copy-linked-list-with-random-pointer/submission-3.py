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
            return None
        
        cur = head
        mirror = {}

        while cur:
            mirror[cur] = Node(cur.val, None, None)
            cur = cur.next
        
        cur = head
        while cur:
            mirror[cur].next = mirror.get(cur.next, None)
            mirror[cur].random = mirror.get(cur.random, None)
            cur = cur.next
        
        return mirror[head]
