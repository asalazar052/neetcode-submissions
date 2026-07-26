class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        # Create the adjacency list
        validTree = True
        adjList = {i:[] for i in range(n)}
        for n1, n2 in edges:
            adjList[n1].append(n2)
            adjList[n2].append(n1)
        
        visited = set()
        # Create dfs function
        def dfs(node, prev):
            nonlocal validTree

            if node in visited: # Base case
                validTree = False
                return

            visited.add(node)
            for neighbor in adjList[node]:
                if neighbor == prev:
                    continue
                dfs(neighbor, node)

        # Call dfs function on 0
        dfs(0, -1)
        return validTree and len(visited) == n

'''
Invalid tree:
1. if there is a cycle
2. if there is an island present

0: [1]
1: [0, 2, 3, 4]
2: [1, 3]
3: [2, 1]
4: [1]

dfs(0, -1) Valid because...
dfs(1, 0) Valid because...
dfs(0, 1)
    
    |-------|
0 - 1 - 2 - 3   4
    |-----------|

A cycle is when we get to a node we've already visited from a node that we havent visited

1 - 4
|
0 - 2
|
3

'''