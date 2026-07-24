class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        # Create adjacency list        
        coursesToPrereqs = {i : [] for i in range(numCourses)}


        '''
        [0,10],[3,18],[5,5],[6,11],[11,14],[13,1],[15,1],[17,4]
        0: 10
        1: 2
        2: 3
        3: 18
        4: 
        5: 5
        '''
        # Load adjacency list
        for course, prereq in prerequisites:
            coursesToPrereqs[course].append(prereq)
        
        possible = True
        visited = set()

        def dfs(cur):
            nonlocal possible
            # Course has no prerequisites
            if not coursesToPrereqs[cur]:
                return

            if cur in visited:
                possible = False
                return
            
            visited.add(cur)
            for prereq in coursesToPrereqs[cur]:
                dfs(prereq)
            visited.remove(cur)

            
        for course, prereq in prerequisites:
            dfs(course)
            
        return possible