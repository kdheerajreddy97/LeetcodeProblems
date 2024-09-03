class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dict = {}
        
        for i, num in enumerate(numbers):
            complement = target- num
            if complement in dict:
                return [dict[complement]+1,i+1]
            dict[num] = i