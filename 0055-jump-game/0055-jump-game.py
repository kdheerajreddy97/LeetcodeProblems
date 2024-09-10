class Solution:
    def canJump(self, nums: List[int]) -> bool:
        position = len(nums) - 1 
        
        for i in range(len(nums)-1,-1,-1):
            if i + nums[i] >= position:
                position = i
        
        return position == 0
        