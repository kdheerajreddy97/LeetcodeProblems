class Solution:
    def findKthLargest(self, nums: List[int], k: int ) -> int:
        min_heap = []
        for i, val in enumerate(nums):
            if len(min_heap) < k:
                heappush(min_heap,val)
            
            elif val > min_heap[0]:
                heappop(min_heap)
                heappush(min_heap, val)
        return heappop(min_heap)



# # Quick Select Method : invloves partition everytime more efficent that heaps
# class Solution:
#     def findKthLargest(self, nums: List[int], k: int) -> int:
#         k = len(nums) - k
        
        
#         def quickselect(l, r):
#             pivot = nums[r]
#             p = l
            
            
#             for index in range(l,r):
#                 if nums[index] <= pivot:
#                     nums[p], nums[index] = nums[index], nums[p]
#                     p +=1
            
#             nums[p], nums[r] = nums[r], nums[p]
            
#             if p > k: 
#                 return quickselect(l, p-1)
#             elif p < k:
#                 return quickselect(p+1, r)
#             else:
#                 return nums[p]
            
#         return quickselect(0,len(nums)-1)
                    
                    
        