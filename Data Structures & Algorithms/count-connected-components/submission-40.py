class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        par = [i for i in range(n)]
        rank = [1] * n

        def find(n1):
            res = n1
            while res != par[res]:
                par[n1] = par[par[n1]]
                res = par[res]

            return res


        def union(n1, n2):

            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return 0
            
            if rank[p1] > rank[p2]:
                par[p2] = p1 # Make the larger tree the parent
                rank[p1] += rank[p2]

            else:
                par[p1] = p2
                rank[p2] += rank[p1]

            return 1
        
        count = n
        for n1, n2 in edges:
            count -= union(n1, n2)
        
        return count
