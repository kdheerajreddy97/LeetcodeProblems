# Time O(n); Space: O(n)
# Just add into the Stack if its a open braces and check if the next character is equal to the top of the stack (else condition)
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
                # Edge case if it starts with closed braces then stack will be empty so return False
                if not mystack or i != mystack[-1]:
                    return False
                else:
                    mystack.pop()
        # Make sure to return true only of if the stack is empty
        return len(mystack) == 0
                
        
        