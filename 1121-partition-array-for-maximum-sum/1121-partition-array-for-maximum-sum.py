# At most K partitions; Exhaustive tree where each node will have k children; repeated subproblems - > dp
# Tabulation: N * K time complexity
class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        dp = [0] * n
        dp[0] = arr[0]

        for i in range(1, n):
            # to cal current max; finding max val of subarray
            currMax = arr[i]
            for j in range(1,k+1):
                if (i - j + 1 >= 0):
                    # calc curr max for finding max val of subarray
                    currMax = max(currMax, arr[i-j+1])
                    # if partition before value exists
                    if (i - j >= 0):
                        dp[i] = max(dp[i], currMax * j + dp[i-j])
                    # if no max subarray before
                    else:
                        dp[i] = max(dp[i], currMax * j)

        return dp[n-1]

        