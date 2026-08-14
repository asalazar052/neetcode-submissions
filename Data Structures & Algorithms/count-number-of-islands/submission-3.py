class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        visited = set() # keep track of points that we already did work on
        q = deque()
        numIslands = 0

        def checkValidity(row, col):
            if row < 0 or row >= ROWS or col < 0 or col >= COLS or (row, col) in visited or grid[row][col] != "1":
                return
            
            q.append((row, col))
            visited.add((row, col))

        def bfs(row, col):
            
            q.append((row, col))
            visited.add((row, col))

            while q:
                curRow, curCol = q.popleft()
                
                checkValidity(curRow - 1, curCol)
                checkValidity(curRow + 1, curCol)
                checkValidity(curRow, curCol - 1)
                checkValidity(curRow, curCol + 1)

        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r, c) not in visited:
                    bfs(r, c)
                    numIslands += 1

        return numIslands