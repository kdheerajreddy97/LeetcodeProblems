class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        length = max(len(a), len(b))
        
        a = a[::-1]
        b = b[::-1]
        
        carry = 0
        output = ""
        
        for i in range(length):
            
            if i < len(a):
               int_a =  int(a[i])
            else:
                int_a = 0
                
            if  i < len(b):
                int_b = int(b[i])
            else:
                int_b = 0
            
            sum = int_a + int_b + carry
            carry = sum // 2 
            sum = str(sum % 2)
            output += sum
        if carry:
            output+= str(carry)
        return output[::-1]
            
            
            
            
            