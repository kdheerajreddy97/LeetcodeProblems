# Bottom-up DP; Time complexity: O(m*n); Space: O(m*n)
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * (n+1) for _ in range(m+1)]
        dp[m-1][n-1] = 1
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                # Edge condition
                if (i == m-1 and j == n-1):
                    continue
                # as per question
                dp[i][j] = dp[i+1][j] + dp[i][j+1]

        return dp[0][0]