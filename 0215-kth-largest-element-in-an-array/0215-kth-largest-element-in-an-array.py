#Time complexity: NLog(k)
class Solution:
    def findKthLargest(self, nums: List[int], k: int ) -> int:
        min_heap = []
        
        for i in range(len(nums)):
            if len(min_heap) < k:
                heappush(min_heap, nums[i])
            elif min_heap[0] <= nums[i]:
                heappop(min_heap)
                heappush(min_heap, nums[i])
        return heappop(min_heap)

