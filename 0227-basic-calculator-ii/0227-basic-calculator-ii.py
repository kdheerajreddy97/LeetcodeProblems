#Can be done in two ways: Either use stack or take 4 variables and follow appraoch similar to expression add operators
class Solution:
    def calculate(self, s: str) -> int:
        
        currval = 0
        lastsign = '+'
        calcval = 0
        tail = 0
        
        
        
        for i in range(len(s)):
            c = s[i]
            
            #check if digit
            if c.isdigit():
                currval = currval * 10 + int(c)
                print(currval)
            
            if ((not c.isdigit()) and (c != ' ')) or i == len(s) - 1:
                
                if lastsign == '+':
                    calcval += currval
                    tail = currval
                elif lastsign == '-':
                    calcval -= currval
                    tail = -currval
                    print(calcval)
                elif lastsign == '*':
                    calcval = (calcval - tail) + (tail * currval)
                    tail = tail * currval
                elif lastsign == '/':
                    calcval = (calcval - tail) + int (tail / currval)
                    tail = int(tail / currval)
                    
                    
                currval = 0
                lastsign = c
        
        return calcval