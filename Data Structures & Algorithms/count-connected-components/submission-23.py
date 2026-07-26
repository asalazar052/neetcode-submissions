class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        par = [i for i in range(n)]
        rank = [1] * n

        # Find the parent of the given node
        def find(n1):
            res = n1
            while res != par[res]:
                par[res] = par[par[res]] # Important line
                res = par[res]
            
            return res
        
        # Union two nodes with the same parent
        def union(n1, n2):
            par1, par2 = find(n1), find(n2)

            if par1 == par2:
                return 0

            if rank[par1] > rank[par2]: # Add smaller tree to bigger tree
                par[par2] = par1
                
            elif rank[par1] < rank[par2]:
                par[par1] = par2
            else:
                rank[par1] += 1
                par[par1] =  par2
            
            return 1

        # Run solution
        counter = n
        for l, r in edges:
            counter -= union(l, r)

        return counter
