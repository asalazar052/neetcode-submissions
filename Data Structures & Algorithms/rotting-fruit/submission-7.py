class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        ROWS, COLS = len(grid), len(grid[0])
        q = deque() # Check if it needs an array inside
        freshCount = 0

        # Loading our queue with rotten fruit
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r, c))
                if grid[r][c] == 1:
                    freshCount += 1 
        
        def checkValidity(row, col):
            nonlocal freshCount

            if row < 0 or row >= ROWS or col < 0 or col >= COLS or grid[row][col] != 1:
                return
            
            grid[row][col] = 2 # Make fruit rotting
            freshCount -= 1
            q.append((row, col))

        minutes = 0
        # Multi-source BFS
        while q and freshCount > 0:

            for _ in range(len(q)):
                r, c = q.popleft()
                checkValidity(r + 1, c)
                checkValidity(r - 1, c)
                checkValidity(r, c + 1)
                checkValidity(r, c - 1)
            
            minutes += 1
        
        if freshCount > 0:
            return -1
        else:
            return minutes