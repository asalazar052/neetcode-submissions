class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        if not n:
            return True

        # Create adjacency list for undirected graph
        adjList = {i:[] for i in range(n)}
        for first, second in edges:
            adjList[first].append(second)
            adjList[second].append(first)

        validTree = True # Tracks whether or not we have a valid tree

        visited = set()
        
        def dfs(node, prev):
            nonlocal validTree

            if node in visited:
                validTree = False
                return
            
            visited.add(node)
            
            for neighbor in adjList[node]:
                
                if neighbor == prev:
                    continue
                dfs(neighbor, node)
                

        dfs(0, -1)
        return validTree and len(visited) == n

'''

dfs(0)
dfs(1)
dfs(0)

0: [1,2,3]
1: [0,4]
2: [0]
3: [0]
4: [1]

When is something not a tree?
1. When it has cycles
'''

        
