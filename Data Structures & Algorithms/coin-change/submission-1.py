class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        dp = [float("inf") for i in range(amount + 1)]
        dp[0] = 0

        for curAmt in range(1, amount + 1):

            for coin in coins:
                if curAmt - coin >= 0: # possible combo 
                    dp[curAmt] = min(1 + dp[curAmt - coin], dp[curAmt])
                # else: # not a possible combo
                #     dp[curAmt] = -1  
        

        if dp[amount] == float("inf"): 
            return -1 
        else:
            return dp[amount]



'''
what is dp[i]?

the solution for the ith amount.

example:
Input: coins = [1,5,10], amount = 12

1:
    dp[0] = 0
5: 
    dp[0] = 0
10:
    dp[0] = 0

1:
    dp[1] = 1 + dp[0]
5:
    dp[1] = -4 -> no soln
10:
    dp[1] = -9 -> no soln

...
1:
    dp[5] = 1 + dp[4]
5:
    dp[5] = 1 + dp[0]


'''
        