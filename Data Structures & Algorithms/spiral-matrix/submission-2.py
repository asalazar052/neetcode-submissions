class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        Top, Bottom = 0, len(matrix)
        Left, Right = 0, len(matrix[0])
        res = []

        while Left < Right and Top < Bottom:
            for i in range(Left, Right):
                res.append(matrix[Top][i])
            Top += 1

            for i in range(Top, Bottom):
                res.append(matrix[i][Right - 1])
            Right -= 1

            if not (Left < Right and Top < Bottom):
                break

            for i in range(Right - 1, Left - 1, -1):
                res.append(matrix[Bottom - 1][i])
            Bottom -= 1

            for i in range(Bottom - 1, Top - 1, -1):
                res.append(matrix[i][Left])
            Left += 1

            
        return res


'''
[x,x,x,x]
[5,6,7,x]
[9,10,11,x]
[x,x,x,x]

1. start at 0,0
(while marking 'x' on the way)
2. go right until you cant anymore (ptr = COLS)
3. go down until you can't anymore (ptr = ROWS)
4. go left until you can't anymore
5. go up till you can't anymore


[[1,2,3,4],[5,6,7,8],[9,10,11,12]]




'''

