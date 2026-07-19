class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS = len(grid)
        COLS = len(grid[0])

        def bfs(row, col):

            q = deque([(row, col, 0)])
            visited = set()
            visited.add((row, col))

            while q:
                cur = q.popleft()

                if grid[cur[0]][cur[1]] == 0:
                    grid[row][col] = cur[2]
                    return
                
                else:
                    if cur[0] + 1 < ROWS and (cur[0] + 1, cur[1]) not in visited and grid[cur[0] + 1][cur[1]] != -1:
                        q.append((cur[0] + 1, cur[1], cur[2] + 1))
                        visited.add((cur[0] + 1, cur[1]))
                    if cur[0] - 1 >= 0 and (cur[0] - 1, cur[1]) not in visited and grid[cur[0] - 1][cur[1]] != -1:
                        q.append((cur[0] - 1, cur[1], cur[2] + 1))
                        visited.add((cur[0] - 1, cur[1]))

                    if cur[1] + 1 < COLS and (cur[0], cur[1] + 1) not in visited and grid[cur[0]][cur[1] + 1] != -1:
                        q.append((cur[0], cur[1] + 1, cur[2] + 1))
                        visited.add((cur[0], cur[1] + 1))

                    if cur[1] - 1 >= 0 and (cur[0], cur[1] - 1) not in visited and grid[cur[0]][cur[1] - 1] != -1:
                        q.append((cur[0], cur[1] - 1, cur[2] + 1))
                        visited.add((cur[0], cur[1] - 1))
                




        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] != 0 and grid[r][c] != -1:
                    bfs(r, c)
        


        
        