class Solution:
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