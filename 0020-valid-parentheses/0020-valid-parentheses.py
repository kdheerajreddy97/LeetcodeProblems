class Solution:
    def isValid(self, s: str) -> bool:
        mystack = []
        
        for i in s:
            if i == '{' or i == '(' or i == '[':
                if i == '{':
                    mystack.append('}')
                elif i == '(':
                    mystack.append(')')
                elif i == '[':
                    mystack.append(']')
            else:
                if not mystack or i != mystack[-1]:
                    return False
                else:
                    mystack.pop()
        return len(mystack) == 0
                
        
        