# 2 Approaches: Bucket Sort or Heaps; For both we need to store the frequency of each element in dictionary
# Approach 1: Bucket Sort; Time: O(n); Space: O(n)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Space: O(n)
        dict = {}
        # Time: O(n)
        for num in nums:
            if num in dict:
                dict[num] += 1
            else:
                dict[num] = 1
        # Space: O(n); Time: O(n); Maximum an element can repeat is "len(nums)" times
        bucket = [[] for _ in range(len(nums) + 1)]
        # Time: O(n)
        for key, val in dict.items():
            bucket[val].append(key)
        
        res = []
        # Time: O(n)
        for i in range(len(bucket)-1, 0, -1):
            for n in bucket[i]:
                res.append(n)
                if len(res) == k:
                    return res
        
            
            
            
            