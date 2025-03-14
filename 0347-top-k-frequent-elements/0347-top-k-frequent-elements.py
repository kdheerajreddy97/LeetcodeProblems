# Using Heaps
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        minheap = []
        n  = len(nums)
        mydict = {}
        res = []

        for num in nums:
            if num in mydict:
                mydict[num] += 1
            else:
                mydict[num] = 1
        
        for num, freq in mydict.items():
            heapq.heappush(minheap, (freq,num))
            if len(minheap) > k:
                heapq.heappop(minheap)
        
        for _ in range(len(minheap)):
            res.append(minheap.pop()[1])
        
        return res
        

        





            
            
            