class Solution:
#  Iterative Approach: Space complexity: O(1) ; Time complexity: O(log(n))
    def myPow(self, x: float, n: int) -> float:
        
        result = 1
        
        if n < 0:
            x = 1/x
            n = -n
            
            
            
        while n != 0:
            if n % 2 != 0:
                result = result * x
            
            n = n//2
            x = x * x
            
        return result


#  Recursive Approach: Space complexity: O(log(n)) ; Time complexity: O(log(n))
        # def myPow(self, x: float, n: int) -> float:
        
        #     if n == 0:
        #         return 1
            
        #     if n < 0:
        #         x = 1/x
        #         n = -n
            
        #     result = self.myPow(x,n//2)
            
            
        #     if n % 2 == 0:
        #         return result * result
        #     else:
        #         return result * result * x
                
        
        
        
        