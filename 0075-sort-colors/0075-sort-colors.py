class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return nums
        dict = {}
        dict[0] = 0
        dict[1] = 0
        dict[2] = 0
        for i in range(len(nums)):
            dict[nums[i]] += 1
        
        for i in range(dict[0]):
            nums[i] = 0
        for i in range(dict[0],dict[0]+ dict[1]):
            nums[i] = 1
        for i in range(dict[0]+ dict[1], dict[0]+ dict[1]+ dict[2]):
            nums[i] = 2
        return nums