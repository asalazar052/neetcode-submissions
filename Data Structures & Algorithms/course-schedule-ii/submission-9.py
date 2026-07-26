class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        # Build our prerequisite map
        courseMap = {i:[] for i in range(numCourses)} # course : prerequisite
        for course, pre in prerequisites:
            courseMap[course].append(pre)
        
        cycle = set() # To detect whether we have a cycle or not
        visited = set() # To make sure we don't revisit nodes

        coursePath = []
        def dfs(crs): # return a boolean of whether or not a configuration is valid

            if crs in cycle: # There is a cycle in our course path, so return empty array
                return False
            if crs in visited:
                return True
            
            cycle.add(crs)
            visited.add(crs)
            for preReq in courseMap[crs]:
                if not dfs(preReq):
                    return False

            cycle.remove(crs)
            coursePath.append(crs)
            return True

        for n in range(numCourses):
            if not dfs(n):
                return []

        return coursePath
            
'''
1 is a prereq to 0
0 : [1]
1 : []

dfs(0)

0 is a prerequisite to 1

0 : []
1 : [0]
2 : []


'''
