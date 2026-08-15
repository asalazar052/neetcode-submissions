class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        dp = [float("inf") for i in range(amount + 1)]
        dp[0] = 0 # Since an amount of 0 can only be made up by 0 coins

        for curAmt in range(1, amount + 1):

            for coin in coins:

                if curAmt - coin >= 0: # Possible combo
                    dp[curAmt] = min(dp[curAmt], 1 + dp[curAmt - coin]) 
                
        
        return -1 if dp[amount] == float("inf") else dp[amount]





'''
What is dp[i]?

The minimum number of coins it takes to make up the exact target amount, for each amount 0 - amount

1 - 1 = 0
min(infinity, dp[0] + 1)

1 - 5 = -4
1 - 10 = -9



'''