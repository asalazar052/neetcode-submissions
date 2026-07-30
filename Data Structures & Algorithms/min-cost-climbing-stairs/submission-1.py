class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        dp = [0 for i in range(len(cost) + 1)]
        dp[len(cost)] = 0 # Costs 0 to reach the final staircase
        dp[len(cost) - 1] = cost[len(cost) - 1] # Costs this amount to reach the final staircase

        for i in range(len(cost)): # Check this, obviously
            idx = len(cost) - 2 - i
            tot1 = cost[idx] + dp[idx + 1]
            tot2 = cost[idx] + dp[idx + 2]
            dp[idx] = min(tot1, tot2)
        
        print(dp)
        return min(dp[0], dp[1])

