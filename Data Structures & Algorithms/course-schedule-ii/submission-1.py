class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        # Build adj list
        coursesToPrereqs = {i:[] for i in range(numCourses)}
        for course, preReq in prerequisites:
            coursesToPrereqs[course].append(preReq)
        
        visited, cycle = set(), set()
        order = []

        def dfs(cur):
            
            if cur in cycle: # Bad
                return False

            if cur in visited: # Good
                return True

            cycle.add(cur)
            for pre in coursesToPrereqs[cur]:
                if dfs(pre) == False:
                    return False
            cycle.remove(cur)
            visited.add(cur)
            order.append(cur)
            return True
        
        for c in range(numCourses):
            if dfs(c) == False:
                return []

        return order




        