class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        if not grid:
            return 0

        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        islands = 0

        def bfs(row, col):

            q = deque([(row, col)])
            visited.add((row, col))

            while q:
                print(q)

                cur = q.popleft()
                curR, curC = cur[0], cur[1]
                
                if curR - 1 >= 0 and grid[curR - 1][curC] != '0' and (curR - 1, curC) not in visited:
                    q.append((curR - 1, curC))
                    visited.add((curR - 1, curC))
                if curC - 1 >= 0 and grid[curR][curC - 1] != '0' and (curR, curC - 1) not in visited:
                    q.append((curR, curC - 1))
                    visited.add((curR, curC - 1))
                if curR + 1 < ROWS and grid[curR + 1][curC] != '0' and (curR + 1, curC) not in visited:
                    q.append((curR + 1, curC))
                    visited.add((curR + 1, curC))
                if curC + 1 < COLS and grid[curR][curC + 1] != '0' and (curR, curC + 1) not in visited:
                    q.append((curR, curC + 1))
                    visited.add((curR, curC + 1))

            


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r, c) not in visited:
                    bfs(r, c)
                    islands += 1
        
        return islands