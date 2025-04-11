# Time: O(n); Space: O(1)
class Solution:
    def myAtoi(self, s: str) -> int:
        sign = 1
        result = 0
        i = 0
    
        INT_MAX = pow(2,31) - 1
        INT_MIN = -pow(2,31)

        s = s.strip()
        n = len(s)
        # Remember by default it takes +
        if i < n and s[i] == '+':
            sign = 1
            i += 1
        # if you dont mention elif(instead of else) it takes negative
        elif i < n and s[i] == '-':
            sign = -1
            i += 1
        
        while i < n and s[i].isdigit():
            digit = int(s[i])
            if (result > INT_MAX //10) or (result == INT_MAX // 10 and digit > INT_MAX % 10):
                if sign == 1:
                    return INT_MAX
                else:
                    return INT_MIN

            result = 10 * result + digit
            i += 1
        
        return result * sign
        
        