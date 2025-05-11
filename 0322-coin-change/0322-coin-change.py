class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        m = len(coins)
        n = amount
        dp = [amount+1] * (n+1)

        dp[0] = 0

        for i in range(1,m+1):
            for j in range(1, n+1):
                if (j >= coins[i-1]):
                    dp[j] = min(dp[j], 1 + dp[j-coins[i-1]])

        if dp[n] != (amount + 1):
            return dp[n]
        else:
            return -1
                

