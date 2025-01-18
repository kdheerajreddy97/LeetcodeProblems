class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # count = {}
        # for num in nums:
        #     if num in count:
        #         count[num] += 1
        #     else:
        #         count[num] = 1

        # for num, ct in count.items():
        #     if ct > len(nums)/2:
        #         return num
        count = 1
        majority = nums[0]
        for i in range(1, len(nums)):
            if nums[i] == majority:
                count +=1 
            else:
                count -= 1

            if count == 0:
                majority = nums[i]
                count = 1

        return majority
