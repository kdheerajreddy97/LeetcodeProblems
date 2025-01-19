class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [1] * n
        prefix[0] = 1
        product = 1
        for i in range(1, n):
            prefix[i] = nums[i-1] * prefix[i-1]
        for i in range(n-2, -1, -1):
            product = product * nums[i+1]
            prefix[i] = prefix[i] * product
        return prefix
