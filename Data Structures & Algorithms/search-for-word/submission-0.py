class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])

        def dfs(r, c, i):
            if i == len(word):
                return True
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or
                word[i] != board[r][c] or board[r][c] == '#'):
                return False

            board[r][c] = '#'
            res = (dfs(r + 1, c, i + 1) or
                   dfs(r - 1, c, i + 1) or
                   dfs(r, c + 1, i + 1) or
                   dfs(r, c - 1, i + 1))
            board[r][c] = word[i]
            return res

        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True
        return False

        # res = False
        # path = set()
        # def search(visited, curWord, x, y):

        #     print(curWord)
        #     if curWord == word:
        #         res = True
        #         return
        #     elif (x - 1 < 0 or (x - 1, y) in visited) and (x + 1 >= len(board[0]) or (x + 1, y) in visited) and (y - 1 < 0 or (x, y - 1) in visited) and (y + 1 >= len(board) or (x, y + 1) in visited):
        #         return

        #     # Left case
        #     if not (x - 1 < 0 or (x - 1, y) in visited):
                
        #         visited.add((x - 1, y))
        #         search(visited, curWord + board[y][x - 1], x - 1, y)
        #         visited.remove((x - 1, y))
            
        #     # Right case
        #     if not (x + 1 >= len(board[0]) or (x + 1, y) in visited):
        #         visited.add((x + 1, y))
        #         search(visited, curWord + board[y][x + 1], x + 1, y)
        #         visited.remove((x + 1, y))
            
        #     # Up case
        #     if not (y - 1 < 0 or (x, y - 1) in visited):
        #         visited.add((x, y - 1))
        #         search(visited, curWord + board[y - 1][x], x, y - 1)
        #         visited.remove((x, y - 1))

        #     # Down case
        #     if not (y + 1 >= len(board) or (x, y + 1) in visited):
        #         visited.add((x, y + 1))
        #         search(visited, curWord + board[y + 1][x], x, y + 1)

        # search(path, "", 0, 0)
        # return res
        


'''
x - 1 < 0
y - 1 < 0
x + 1 > len(board[0])
y + 1 > len(board)

cur not in 


'''
            

            

        