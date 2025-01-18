# Approach1: Exhaustive search -> Choose dont choose scenario
# Approach2: using states for buy and sell (not optimized but will be helpful in memoization)
# Approach3: Recursion with memoization - Bottom to top
# Approach4: Tabulation
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n <= 1:
            return 0
        dp = [[0 for _ in range(2)] for _ in range(n)]
        print(dp)

        dp[0][0] = -prices[0]
        dp[1][0] = max(-prices[0], -prices[1])
        dp[1][1] = max(dp[0][1], dp[0][0] + prices[1])

        for i in range(2,n):
            # Not Buy; Buy
            dp[i][0] = max(dp[i-1][0], dp[i-2][1] - prices[i] )
            # Not Sell; Sell
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] + prices[i])
        
        return dp[n-1][1]
        