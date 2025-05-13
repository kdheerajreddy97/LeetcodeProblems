# DP:Only one decision making parameter
# Time: O(n); Space: O(n)
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
             return nums[0]

        dp = [0] * (n + 1)
        dp[1] = nums[0]

        for i in range(2,n+1):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i-1])
            print(dp[i])
        return dp[n]