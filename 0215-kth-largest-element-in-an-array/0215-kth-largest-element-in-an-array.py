#Time complexity: N + kLog(N)
class Solution:
    def findKthLargest(self, nums: List[int], k: int ) -> int:
        max_heap = []

        for num in nums:
            heappush(max_heap, -num)
        
        for i in range(k-1):
            heappop(max_heap)
        return -heappop(max_heap)
        
