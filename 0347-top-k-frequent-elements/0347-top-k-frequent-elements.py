# Brute force
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict = {}
        res = []
        for num in nums:
            if num in dict:
                dict[num] += 1
            else:
                dict[num] = 1
        
        
        my_dict = sorted(dict.items(), key = lambda item:item[1], reverse = True)
       
        for key,val in my_dict:
            if k == 0:
                return res
            res.append(key)
            k -= 1
        return res





            
            
            