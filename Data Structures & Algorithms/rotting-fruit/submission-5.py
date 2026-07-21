class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        q = deque([])
        healthy_trees = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r,c))
                elif grid[r][c] == 1:
                    healthy_trees += 1
                    
        # no burning trees
        if healthy_trees == 0:
            return 0
        if not q:
            return -1
        
        "If it is impossible for every healthy tree to catch fire, return `-1`."

        # [0], [1], [2]
        # r * c
        visited = set()

        # multi-source BFS
        minutes = 0
        while q and healthy_trees > 0:
            # look at neighbors
            for _ in range(len(q)):
                r,c = q.popleft()
                directions = [(0,1), (0,-1), (1,0), (-1,0)]
                for dr, dc in directions:
                    nr, nc = dr + r, dc + c
                    if nc in range(COLS) and nr in range(ROWS) and grid[nr][nc] == 1 and (nr,nc) not in visited:
                        q.append((nr,nc))
                        visited.add((nr,nc))
                        healthy_trees -= 1

            minutes += 1

        if healthy_trees > 0:
            return -1

        return minutes




'''
Impossible with an island in the grid
Can use BFS, traversing every second

Should be able to complete with 1 BFS

211
110
011
'''