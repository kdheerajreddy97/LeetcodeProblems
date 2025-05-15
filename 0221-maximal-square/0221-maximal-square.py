# Brute Force approach; Time: O(m2*n2) - go over each cell(M*N) - For each cell check the diagonal if 1 then iterate along row and column to check if its 1; follow this till it breaks (finds 0)
# DP Approach: Time: O(m*n); Space:O(m*n)
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        largest = 0
        dp = [[0] * (n + 1) for _ in range(m+1)]
        
        for i in range(1,m+1):
            for j in range(1,n+1):
                if matrix[i-1][j-1] == "1":
                    dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
                    largest = max(dp[i][j], largest)
        
        return largest*largest
        