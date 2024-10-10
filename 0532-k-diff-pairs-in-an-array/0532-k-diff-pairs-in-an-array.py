class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        values = {}
        res = 0
        for num in nums:
            if num in values:
                values[num] +=1
            else:
                values[num] = 1
        print(values)
            
        for key, val in values.items():
            diff = k + key
            if k > 0 and diff in values:
                res+=1
            if k == 0 and val > 1:
                res += 1

        return res
            
                
            
        