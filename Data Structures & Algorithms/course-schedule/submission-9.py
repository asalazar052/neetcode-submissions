class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        courseMap = {i:[] for i in range(numCourses)}
        for c, p in prerequisites:
            courseMap[c].append(p)

        valid = True
        visited = set()
        def dfs(course):
            nonlocal valid

            if course in visited:
                valid = False
                return
            if courseMap[course] == []:
                return

            visited.add(course)
            for p in courseMap[course]:
                dfs(p)
            visited.remove(course)
            courseMap[course] = []

        for c, p in prerequisites:
            dfs(c)
        
        return valid
