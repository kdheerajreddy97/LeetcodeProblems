class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = []

        for num in nums:
            heapq.heappush(min_heap, num)
            # Pop once heap size reaches k - N * LogK(Time)
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        return min_heap[0]
