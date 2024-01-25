class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict = {}
        out = []
        for num in nums:
            if num in dict:
                dict[num]  +=1
            else:
                dict[num] = 1
                
        for _ in range(k):
            max_key = max(dict, key = dict.get)
            out.append(max_key)
            del dict[max_key]
        
        return out
            
        