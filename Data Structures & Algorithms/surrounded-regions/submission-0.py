class Solution:
    def solve(self, board: List[List[str]]) -> None:

        ROWS, COLS = len(board), len(board[0])
        interested = []

        # Load up the cells of interested
        for r in range(ROWS):
            if board[r][0] == "O":
                interested.append((r, 0))
            if board[r][COLS - 1] == "O":
                interested.append((r, COLS - 1))
        for c in range(COLS):
            if board[0][c] == "O":
                interested.append((0, c))
            if board[ROWS - 1][c] == "O":
                interested.append((ROWS - 1, c))

        def dfs(r, c, visited):
            if (r, c) in goodCells or r < 0 or r >= ROWS or c < 0 or c >= COLS or board[r][c] != "O":
                return
            
            visited.add((r, c))
            dfs(r + 1, c, visited)
            dfs(r - 1, c, visited)
            dfs(r, c + 1, visited)
            dfs(r, c - 1, visited)
        
        goodCells = set()
        for c in interested:
            row, col = c
            dfs(row, col, goodCells)
        
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) not in goodCells and board[r][c] == "O":
                    board[r][c] = "X"
'''
Plan:
- Find all 'O' cells on the edge of the board
- DFS all of them to find which what cells withinb the board are part of the region that touches
the edge    
- Loop through all cells. Anything that is an O and is not in visited mark as X

'''