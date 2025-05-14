class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        n = len(nums)
        max_number = max(nums)
        points = [0] * (max_number+1)

        for num in nums:
            points[num] += num
        m = len(points)
        dp = [0] * len(points)

        dp[0] = 0
        dp[1] = points[1]

        for i in range(2,len(points)):
            dp[i] = max(dp[i-1], points[i] + dp[i-2])

        return dp[m-1]
            