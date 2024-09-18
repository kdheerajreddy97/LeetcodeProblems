class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l,r = 0,0
        
        for r in range(0, len(nums)):
            if nums[r]:
                nums[l] , nums[r] = nums[r], nums[l]
                l +=1
        return nums 