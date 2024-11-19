#Can be done in two ways: Either use stack or take 4 variables and follow approach similar to expression add operators
# class Solution:
#     def calculate(self, s: str) -> int:
        
#         currval = 0
#         lastsign = '+'
#         calcval = 0
#         tail = 0
        
        
        
#         for i in range(len(s)):
#             c = s[i]
            
#             #check if digit
#             if c.isdigit():
#                 currval = currval * 10 + int(c)
            
#             if ((not c.isdigit()) and (c != ' ')) or i == len(s) - 1:
                
#                 if lastsign == '+':
#                     calcval += currval
#                     tail = currval
#                 elif lastsign == '-':
#                     calcval -= currval
#                     tail = -currval
#                 elif lastsign == '*':
#                     calcval = (calcval - tail) + (tail * currval)
#                     tail = tail * currval
#                 elif lastsign == '/':
#                     calcval = (calcval - tail) + int (tail / currval)
#                     tail = int(tail / currval)
                    
                    
#                 currval = 0
#                 lastsign = c
        
#         return calcval



#Using Stack

class Solution:
    def calculate(self, s: str) -> int:
        
        currval = 0
        lastsign = '+'
        
        mystack = []
        res = 0
    
        for i in range(len(s)):
            c = s[i]
            
            #check if digit
            if c.isdigit():
                currval = currval * 10 + int(c)
            
            if ((not c.isdigit()) and (c != ' ')) or i == len(s) - 1:
                
                if lastsign == '+':
                    mystack.append(currval)
                elif lastsign == '-':
                    mystack.append(-currval)
                elif lastsign == '*':
                    temp = mystack.pop()
                    mystack.append(temp * currval)
                elif lastsign == '/':
                    temp = mystack.pop()
                    mystack.append(int(temp / currval))
                    
                    
                currval = 0
                lastsign = c
                
        for i in range(len(mystack)):
            res += mystack.pop()
        
        return res