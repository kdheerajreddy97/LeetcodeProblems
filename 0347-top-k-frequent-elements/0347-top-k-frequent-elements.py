# Using Heaps: min_heap: Time: O(nlogk); Space: O(n)
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
            # Inserting in to minheap till k
            heapq.heappush(minheap, (freq,num))
            # start popping after k
            if len(minheap) > k:
                heapq.heappop(minheap)
        
        for freq, num in minheap:
            res.append(num)
        
        return res
        

        





            
            
            