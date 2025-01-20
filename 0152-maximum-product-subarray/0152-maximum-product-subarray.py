# Kadane's Algorithmn: O(n)
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # Time limit exceded: O(n2)
        # n = len(nums)
        # max_product = nums[0]
        # for i in range(n):
        #     curr_product = 1
        #     for j in range(i,n):
        #         curr_product = curr_product * nums[j]
        #         max_product = max(max_product, curr_product)
        # return max_product

        n = len(nums)
        curr_min = nums[0]
        curr_max = nums[0]
        max_product = nums[0]
        for i in range(1,n):
            num = nums[i]

            if num < 0:
                curr_min, curr_max = curr_max, curr_min

            curr_max = max(curr_max * num, num)
            curr_min = min(curr_min * num, num)
            max_product = max(max_product, curr_max)
        return max_product

