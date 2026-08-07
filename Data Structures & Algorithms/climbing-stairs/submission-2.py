class Solution:
    def climbStairs(self, n: int) -> int:
        
        if n < 1:
            return 0
        a0, a1 = 0, 1

        for i in range(n):

            temp = a0 + a1
            a0 = a1
            a1 = temp

        return a1




'''
2: Jump 2 at once or jump 1 twice

3: jump 2, then 1; jump 1, then two; jump 1 3 times.


'''
        