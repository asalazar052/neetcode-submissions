class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        maxArea = 0

        # runs for a single island, so return the area and compare to max area
        def bfs(row, col):
            
            curArea = 0
            q = deque([(row, col)])
            while q:
                cur = q.popleft()
                curR, curC = cur[0], cur[1]
                curArea += 1

                # Down
                if (curR - 1, curC) not in visited and curR - 1 >= 0 and grid[curR - 1][curC] == 1:
                    visited.add((curR - 1, curC))
                    q.append((curR - 1, curC))
                
                # Left
                if (curR, curC - 1) not in visited and curC - 1 >= 0 and grid[curR][curC - 1] == 1:
                    visited.add((curR, curC - 1))
                    q.append((curR, curC - 1))
                
                # Up
                if (curR + 1, curC) not in visited and curR + 1 < ROWS and grid[curR + 1][curC] == 1:
                    visited.add((curR + 1, curC))
                    q.append((curR + 1, curC))
                
                # Right
                if (curR, curC + 1) not in visited and curC + 1 < COLS and grid[curR][curC + 1] == 1:
                    visited.add((curR, curC + 1))
                    q.append((curR, curC + 1))

            return curArea


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    visited.add((r, c))
                    maxArea = max(maxArea, bfs(r, c))
        
        return maxArea
        