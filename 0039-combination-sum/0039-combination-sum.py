class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # 0-1 based recursion
        
        res = []
        
        def helper(nums, i, target,path):
            #Base case
            if target == 0:
                res.append(path[:])
                return
            
            if target < 0 or i == len(nums):
                return
            
            #Dont choose
            #Recurse
            helper(nums, i+1, target, path)
            #Choose
            #Action
            target = target - nums[i]
            path.append(nums[i])
            #Recurse
            helper(nums, i, target, path)
            #Back track
            path.pop()
        
        helper(candidates, 0, target, [])
        return res
            