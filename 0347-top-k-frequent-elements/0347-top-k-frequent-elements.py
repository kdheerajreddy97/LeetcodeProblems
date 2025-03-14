# Using Heaps: min_heap: Time: O(nlogk); Space: O(n)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        mydict = {}
        n = len(nums)
        res = []

        for num in nums:
            if num in mydict:
                mydict[num] += 1
            else:
                mydict[num] = 1
        
        buckets = [[] for i in range(n+1)]

        for num,freq in mydict.items():
            buckets[freq].append(num)
        
        for i in range(len(buckets)-1,-1,-1):
            for n in buckets[i]:
                res.append(n)
                if len(res) == k:
                    return res

            

        





            
            
            