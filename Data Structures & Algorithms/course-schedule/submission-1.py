class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        # map each course to prereq list
        preMap = { i : [] for i in range(numCourses)}

        for crs, pre in prerequisites:
            preMap[crs].append(pre) # add all prereqs
        
        visited = set()
        def dfs(crs):
            # Cycle detected
            if crs in visited:
                return False
            
            # No prereqs required
            if preMap[crs] == []:
                return True
            
            # Backtracking
            visited.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            visited.remove(crs)

            #preMap[crs] = [] # So we don't have to do more work
            return True
        
        for i in range(numCourses):
            if not dfs(i): return False
        
        return True
        
