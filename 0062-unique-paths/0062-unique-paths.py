# Normal recursive approach; Time complexity : 2^(m+n)
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = [[0] * n for _ in range(m)]

        def helper(i,j):
            if (i == m-1 and j == n-1):
                return 1
            if (i >= m or j >=n):
                return 0
            if memo[i][j] != 0:
                return memo[i][j]
                
            cost1 = helper(i, j+1)
            cost2 = helper(i+1, j)

            memo[i][j] = cost1 + cost2

            return memo[i][j]

        return helper(0,0)