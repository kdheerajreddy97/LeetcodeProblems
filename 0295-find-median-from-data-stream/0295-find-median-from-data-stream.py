class MedianFinder:

    def __init__(self):
        self.small = [] # max_heap
        self.large = [] # min_heap

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -1 * num)

        # check if the number inserted in max_heap is smaller than the number in min_heap
        if(self.small and self.large and (-1 * self.small[0]) > self.large[0]):
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        
        # Uneven size
        if len(self.small) > len(self.large) + 1:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        
        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * val)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large): 
            return -1 * self.small[0]
        if len(self.small) < len(self.large):
            return self.large[0]
        else:
            return (-1 * self.small[0] + self.large[0]) / 2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()