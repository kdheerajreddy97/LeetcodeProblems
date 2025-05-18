# Bucket Sort
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_val = min(nums)
        max_val = max(nums)
        n = len(nums)

        buckets = [0] * (max_val - min_val + 1)

        for num in nums:
            buckets[num - min_val] += 1
        
        for i in range(max_val - min_val, -1, -1):
            while buckets[i] > 0:
                buckets[i] -= 1
                k -= 1
                if k == 0:
                    return i + min_val

        