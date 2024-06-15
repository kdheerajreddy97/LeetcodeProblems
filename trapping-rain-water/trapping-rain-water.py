class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0 
        r = len(height) - 1
        max_left = height[l]
        max_right = height[r]
        trapped_water = 0
        
        if len(height) == 0:
            return 0
        
        while l < r:
            
            if max_left < max_right:
                l +=1
                max_left = max(max_left, height[l])
                trapped_water += max_left - height[l]

                
            else:
                r -=1
                max_right = max(max_right, height[r])
                trapped_water += max_right - height[r]

                
        return trapped_water
            
        
            
                
            
        