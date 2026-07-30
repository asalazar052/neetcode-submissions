class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        # dp = [0 for i in range(len(cost) + 1)]
        two = 0 # Costs 0 to reach the final staircase
        one = cost[len(cost) - 1] # Costs this amount to reach the final staircase

        for i in range(len(cost) - 1): # Check this, obviously
            idx = len(cost) - 2 - i
            total = min(cost[idx] + one, cost[idx] + two)
            temp = one
            one = total
            two = temp
        
        
        return min(one, two)

