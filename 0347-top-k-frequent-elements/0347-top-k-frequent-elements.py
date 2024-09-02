class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict = {}
        for num in nums:
            if num in dict:
                dict[num] += 1
            else:
                dict[num] = 1
        
        bucket = [[] for _ in range(len(nums) + 1)]
        
        for key, val in dict.items():
            bucket[val].append(key)
        
        res = []
        
        for i in range(len(bucket)-1, 0, -1):
            for n in bucket[i]:
                res.append(n)
                if len(res) == k:
                    return res
        
            
            
            
            