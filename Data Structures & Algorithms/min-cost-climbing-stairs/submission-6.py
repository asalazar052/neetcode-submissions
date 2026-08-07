class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        pay1, pay2 = 0, 0

        for c in cost:
            temp = min(pay1 + c, pay2 + c)
            pay1 = pay2
            pay2 = temp
        
        return min(pay1, pay2)