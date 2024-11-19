class Solution:
    
    def __init__(self):
        self.idx = 0
    
    def calculate(self, s: str) -> int:
        
        currval = 0
        lastsign = '+'
        calcval = 0
        tail = 0
        n = len(s)
        
        
        while self.idx < n:
            c = s[self.idx]
            self.idx += 1
            
            #check if digit
            if c.isdigit():
                currval = currval * 10 + int(c)
                
            elif c == '(':
                currval = self.calculate(s)
            
            if ((not c.isdigit()) and (c != ' ')) or self.idx == n:
                
                if lastsign == '+':
                    calcval += currval
                    tail = currval
                elif lastsign == '-':
                    calcval -= currval
                    tail = -currval
                # elif lastsign == '*':
                #     calcval = (calcval - tail) + (tail * currval)
                #     tail = tail * currval
                # elif lastsign == '/':
                #     calcval = (calcval - tail) + int (tail / currval)
                #     tail = int(tail / currval)
                    
                if c == ')':
                    return calcval
                
                currval = 0
                lastsign = c
        
        return calcval