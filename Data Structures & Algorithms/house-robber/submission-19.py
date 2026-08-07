class Solution:
    def rob(self, nums: List[int]) -> int:
        
        rob1, rob2 = 0, 0

        for n in nums:
            
            temp = max(rob1 + n, rob2) # Maximum between robbing the current house and robbing 2 houses before OR only robbing the previous hosue
            rob1 = rob2
            rob2 = temp
        
        return rob2