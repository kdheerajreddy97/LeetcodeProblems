class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
            
        for i, key in enumerate(nums):
            diff = target-key
            if diff in dict:
                return [i,dict[diff]]
            dict[key] = i
            
            
            
            
            
            
            
            
        