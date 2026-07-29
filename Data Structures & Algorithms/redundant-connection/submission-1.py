class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        par = [i for i in range(len(edges) + 1)]
        rank = [1] * (len(edges) + 1)

        def find(n1):
            res = n1

            while res != par[res]:
                par[res] = par[par[res]]
                res = par[res]

            return res
        
        def union(n1, n2):

            p1, p2 = find(n1), find(n2)
            
            # Already in the same group, redundant edge
            if p1 == p2:
                return False
            
            # Not in the same group, so group them
            if rank[p1] > rank[p2]:
                par[p2] = p1 
                rank[p1] += rank[p2]

            else:
                par[p1] = p2
                rank[p2] += rank[p1]
            
            return 1
        
        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2]
            