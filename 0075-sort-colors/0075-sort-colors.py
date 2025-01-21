# Approach take 3 pointers; low = , mid =0, high = n - if mid =0; swap with left and increment both; if 1 increment; else decrement high
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        low = 0
        high = len(nums) -1
        mid = 0
        
        while (mid <= high):
            if nums[mid] == 0:
                temp = nums[low]
                nums[low] = nums[mid]
                nums[mid] = temp
                
                low += 1
                mid += 1

            elif nums[mid] == 1:
                mid += 1
            else:
                temp = nums[high]
                nums[high] = nums[mid]
                nums[mid] = temp
                
                high -= 1
        return nums