class Solution:
    def climbStairs(self, n: int) -> int:
        
        # Represents (n-1)th stair and nth stair
        one, two = 1, 1
        
        for i in range(n - 1):
            temp = one
            one = one + two
            two = temp
        
        return one
'''
[_,3,2,1,1]

'''
