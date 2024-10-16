class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        count = 0
        filteredStr = []
        res = []
        for char in s:
            if char == '(':
                count += 1
                filteredStr.append(char)
            elif char == ')' and count > 0:
                count -= 1
                filteredStr.append(char)
                
            elif char != ')':
                filteredStr.append(char)
                
        
        filteredStr = "".join(filteredStr)
        
        for char in filteredStr[::-1]:
            if char == '(' and count > 0:
                count-=1
            else:
                res.append(char)
        return "".join(res[::-1])
                
                
                