class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        ROWS = len(board)
        COLS = len(board[0])
        visited = set()
        res = False
        
        def search(curR, curC, curLen):
            nonlocal res

            if curLen == len(word):
                res = True
                return
            
            if curR < 0 or curR >= ROWS or curC < 0 or curC >= COLS or board[curR][curC] == '#' or board[curR][curC] != word[curLen]:
                return

            # visited.add((curR, curC))
            temp = board[curR][curC]
            board[curR][curC] = '#'
            search(curR + 1, curC, curLen + 1)
            search(curR - 1, curC, curLen + 1)
            search(curR, curC + 1, curLen + 1)
            search(curR, curC - 1, curLen + 1)
            board[curR][curC] = temp
            # visited.remove((curR, curC))


        for r in range(ROWS):
            for c in range(COLS):
                search(r, c, 0)
        
        return res


'''
Time: O(m * n * 4^w) 
Space: O(n)
m = rows, n = cols, w = len(word)

'''