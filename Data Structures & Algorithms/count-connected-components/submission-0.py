class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        adjList = {i:[] for i in range(n)}
        for n1, n2 in edges:
            adjList[n1].append(n2)
            adjList[n2].append(n1)
        
        visited = set()
        counter = 0
        def dfs(node):
            nonlocal counter

            if node in visited: # Base case
                return
            
            visited.add(node)
            for neighbor in adjList[node]:
                dfs(neighbor)


        for i in range(n):
            if i in visited:
                continue
            else:
                counter += 1
                dfs(i)
        
        return counter
'''
Loop for all n values

1. Check if it is in visited: If it is, return, if it is not, increment counter by 1 
'''