class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        curr_sum = nums[0]
        max_sum = nums[0]
        for i in range(1, n):
            curr_sum += nums[i]
            curr_sum = max(curr_sum, nums[i])
            max_sum = max(max_sum, curr_sum)
        return max_sum
 
            