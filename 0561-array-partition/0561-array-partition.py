# 2 Approaches:
# 1. Sort the array and then compare consecutive numbers, get minimum then add to maximize: O(nlog(n))
# 2. Bucket Sort: O(range of numbers) // use dictionary
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        res = 0
        for i in range(0,len(nums),2):
            res += nums[i]
            
        return res