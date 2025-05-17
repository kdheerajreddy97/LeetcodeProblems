# Exhaustive Tree -> Reapeating Subproblems -> DP
# 2 pointer -> 2 variables: 2-D DP Bottom up approach - Tabulation
# Time: O(m*n) ; Space: O(m*n)
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        # Construct the 2-D DP table; "+1" for empty string case
        dp = [[float("inf")] * (n+1) for _ in range(m+1)]

        # Empty string case i.e. length(non-empty string)
        for i in range(len(word1)+ 1):
            dp[i][len(word2)] = len(word1) - i
        for j in range(len(word2)+1):
            dp[len(word1)][j] = len(word2) - j
        
        # start filling from end index
        for i in range(len(word1)-1,-1,-1):
           for j in range(len(word2)-1,-1,-1):
            # Equal cond - No operation
            if word1[i] == word2[j]:
                dp[i][j] = dp[i+1][j+1]
            else:
                # min of insert, delete, replace
                # 1. insert - dp[i][j+1]
                # 2. delete - dp[i+1][j]
                # 3. replace - dp[i+1][j+1]
                dp[i][j] = 1 + min(dp[i][j+1], dp[i+1][j], dp[i+1][j+1])
        return dp[0][0]

        