class Solution:
    def rob(self, nums: List[int]) -> int:
        
        m = len(nums)
        
        if m == 0:
            return 0

        dp = [0] * m
        dp[0] = nums[0]    
        
        
        for i in range(1,m):
            dp[i] = max(nums[i] + dp[i-2], dp[i-1])
        
        
        return dp[m-1]