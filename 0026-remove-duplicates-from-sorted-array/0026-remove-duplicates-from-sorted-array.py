class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = 0
        slow = 0 
        fast = 0
        n = len(nums)

        while (fast < n):
            if fast > 0 and nums[fast] == nums[fast-1]:
                count += 1
            else:
                count = 1
            
            if count <= 1:
                nums[slow] = nums[fast]
                slow += 1
            
            fast += 1
        return slow
