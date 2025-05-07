class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        n = len(nums)

        def helper(path, pivot):
            res.append(path[:])
            
            for i in range(pivot, n):
                if i > pivot and nums[i] == nums[i-1]:
                    continue
                path.append(nums[i])
                helper(path, i + 1)
                path.pop()

        helper([], 0)
        return res