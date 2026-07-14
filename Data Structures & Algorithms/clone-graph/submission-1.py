"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        if not node:
            return None

        mapper = {} # original : new
        def dfs(cur):

            if cur in mapper:
                return mapper[cur]
            
            mapper[cur] = Node(cur.val)
            for n in cur.neighbors:
                mapper[cur].neighbors.append(dfs(n))
            return mapper[cur]    
            
        dfs(node)
        return mapper[node]
'''
start at 1
1 is not in mapper, so continue
add 1 to mapper

for all of 1's neighbors, check if they are in mapper


'''

