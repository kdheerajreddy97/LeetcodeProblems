# Exhaustive search - Repeated Sub problems - DP - tabulation
# Time: O(m*n); Space: O(m*n)
# Approach 1: DP -Tabulation - 2D
# class Solution:
#     def isMatch(self, s: str, p: str) -> bool:
#         m = len(s)
#         n = len(p)

#         dp = [[False] * (n+1)  for _ in range(m + 1)]
#         # Empty Strings
#         dp[0][0] = True
#         # Fill the first column
#         for j in range(1,n+1):
#             # 1 Step Back
#             if p[j-1] == '*':
#                 dp[0][j] = dp[0][j-1]
        
#         for i in range(1, m+1):
#             for j in range(1,n+1):
#                 # 1 step back: dp[i][j-1] (OR) 1 step above: dp[i-1][j]
#                 if p[j-1] == '*':
#                     dp[i][j] = dp[i][j-1] or dp[i-1][j]
#                 # Diagonal: dp[i-1][j-1]
#                 elif p[j-1] == s[i-1] or p[j-1] == '?':
#                     dp[i][j] = dp[i-1][j-1]
#                 else:
#                     dp[i][j] = False
#         return dp[m][n]

# Approach 2: DP -Tabulation - 1D
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m = len(s)
        n = len(p)

        dp = [False] * (n+1)
        # Empty Strings
        dp[0] = True
        # Fill the first column
        for j in range(1,n+1):
            # 1 Step Back
            if p[j-1] == '*':
                dp[j] = dp[j-1]
        
        for i in range(1, m+1):
            diagup = dp[0]
            dp[0] = False
            for j in range(1,n+1):
                temp = dp[j]
                # 1 step back: dp[i][j-1] (OR) 1 step above: dp[i-1][j]
                if p[j-1] == '*':
                    dp[j] = dp[j-1] or dp[j]
                # Diagonal: dp[i-1][j-1]
                elif p[j-1] == s[i-1] or p[j-1] == '?':
                    dp[j] = diagup
                else:
                    dp[j] = False
                diagup = temp
        return dp[n]


        
        