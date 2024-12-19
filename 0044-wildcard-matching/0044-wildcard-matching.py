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
#                 # Dont choose: 1 step back: dp[i][j-1] (OR) choose: 1 step above: dp[i-1][j]
#                 if p[j-1] == '*':
#                     dp[i][j] = dp[i][j-1] or dp[i-1][j]
#                 # Diagonal: dp[i-1][j-1]
#                 elif p[j-1] == s[i-1] or p[j-1] == '?':
#                     dp[i][j] = dp[i-1][j-1]
#                 else:
#                     dp[i][j] = False
#         return dp[m][n]

# Approach 2: DP -Tabulation - 1D
# class Solution:
#     def isMatch(self, s: str, p: str) -> bool:
#         m = len(s)
#         n = len(p)

#         dp = [False] * (n+1)
#         # Empty Strings
#         dp[0] = True
#         # Fill the first column
#         for j in range(1,n+1):
#             # 1 Step Back
#             if p[j-1] == '*':
#                 dp[j] = dp[j-1]
        
#         for i in range(1, m+1):
#             diagup = dp[0]
#             dp[0] = False
#             for j in range(1,n+1):
#                 temp = dp[j]
#                 # Dont choose: 1 step back: dp[j-1] (OR) choose: 1 step above: dp[j]
#                 if p[j-1] == '*':
#                     dp[j] = dp[j-1] or dp[j]
#                 # Diagonal: dp[i-1][j-1]
#                 elif p[j-1] == s[i-1] or p[j-1] == '?':
#                     dp[j] = diagup
#                 else:
#                     dp[j] = False
#                 diagup = temp
#         return dp[n]


# Approach 3: DP - Recursion with Memoization
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m = len(s)
        n = len(p)
        self.memo = [[None] *n for _ in range(m)]
        return self.helper(s, p, 0, 0)

    def helper(self, s, p, i, j):
        # Base Case
        # Both reach the end of the string
        if i == len(s) and j == len(p):
            return True
        # If Pattern each end of the string
        elif j == len(p):
            return False
        # If String reaches end and if pattern has *'s
        elif i == len(s):
            for k in range(j, len(p)):
                if p[k] != '*':
                    return False
            return True

        if self.memo[i][j] != None:
             return self.memo[i][j]
        # Logic
        result = False
        # If 2 characters match then increment both pointers
        if s[i] == p[j] or p[j] == '?':
            result = self.helper(s, p, i+1, j+1)
        elif p[j] == '*':
                        # Dont Choose                     # Choose
            result = self.helper(s, p, i, j+1) or self.helper(s, p, i+1, j)
        
        self.memo[i][j] = result
        return result

        