# Normal approach take pointers for each string and compare. But we have to do exhausitve search beacuse of the regular expressions; Time: 2^(M*n)
# Teh decision can be based only on *;
# Think of the problem from brute force perspective - we have to do memoization
# Exhaustive Tree -> Repeating Subproblems -> DP
# 2 pointer -> 2 variables: 2-D DP Bottom up approach - Tabulation
# Time: O(m*n); Space: O(m*n)
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m = len(s)
        n = len(p)
        # Using 1- based indexing in DP table
        dp = [[False] * (n+1) for _ in range(m+1)]
        # Base Case: Both empty pattern match
        dp[0][0] = True
        # Base Case: Handle patterns with * that matches empty strings
        for j in range(2, n+1):
            if p[j-1] == '*':
                dp[0][j] = dp[0][j-2] # 2 Steps Back

        for i in range(1, m+1):
            for j in range(1, n+1):
                # Character match - Diagonal left
                if p[j-1] == s[i-1] or p[j-1] == ".":
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == "*":
                    # No choose case - 2 steps back
                    dp[i][j] = dp[i][j-2]
                    # Choose case - straight above
                    if p[j-2] == s[i-1] or p[j-2] == '.':
                        dp[i][j] = dp[i][j] or dp[i-1][j]

        return dp[m][n]
                

        