class Solution:
    def climbStairs(self, n: int) -> int:
        

        a0, a1 = 1, 1

        for i in range(n):

            temp = a0 + a1
            a0 = a1
            a1 = temp

        return a0




'''
2: Jump 2 at once or jump 1 twice

3: jump 2, then 1; jump 1, then two; jump 1 3 times.


'''
        