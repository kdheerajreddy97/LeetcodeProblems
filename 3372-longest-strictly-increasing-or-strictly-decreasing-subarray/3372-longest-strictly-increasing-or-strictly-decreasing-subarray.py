class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        count = 1
        longest = 0

        if len(nums) == 1:
            return len(nums)

        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                count += 1
            else:
                count = 1
            longest = max(longest, count)
        count = 1
        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                count += 1
            else:
                count = 1
            longest = max(longest, count)
        return longest