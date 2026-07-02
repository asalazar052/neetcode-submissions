class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        ROWS = len(board)
        COLS = len(board[0])
        visited = set()
        res = False

        def search(i, r, c, cur):
            
            nonlocal res
            if i == len(word):
                res = True
                return 
            
            #  Out of bounds
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or word[i] != board[r][c] or (r, c) in visited:
                return
            
            cur += board[r][c]
            visited.add((r, c))
            search(i + 1, r + 1, c, cur)
            search(i + 1, r - 1, c, cur)
            search(i + 1, r, c + 1, cur)
            search(i + 1, r, c - 1, cur)
            visited.remove((r, c))

            return

        for r in range(ROWS):
            for c in range(COLS):    
                search(0, r, c, "")

        return res
            


            
        


'''
x - 1 < 0
y - 1 < 0
x + 1 > len(board[0])
y + 1 > len(board)

cur not in 


'''
            

            

        