# Similar to daily Temperatures question but it since its circular we need to iterate over it twice to find next greater number
# 
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        mystack = []
        res = [-1] * n
        
        
        for i in range(2*n):
            while mystack and nums[mystack[-1]] < nums[i%n]:
                temp = mystack.pop()
                next_greater = nums[i%n]
                res[temp] = next_greater
            
            if res[i%n] == -1:
                mystack.append(i%n)
            
        return res