class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        res = []
        for point in points:
            x, y = point
            distance = x **2 + y **2
            minHeap.append([distance,x,y])
            
        heapq.heapify(minHeap)
        
        for i in range(k):
            distance, x, y = heapq.heappop(minHeap)
            res.append([x,y])
        return res