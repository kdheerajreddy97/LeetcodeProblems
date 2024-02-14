class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = ""
        for c in s:
            if self.isalnum(c) == True:
                res += c.lower()
            l = 0
            r = len(res) - 1
        while l< r:
            if res[l] != res[r]:
                return False
            l +=1
            r -=1
        return True
        
        
        
    def isalnum(self, c: str) -> bool:
        if ((ord('A') <= ord(c) <= ord('Z'))  | (ord('a') <= ord(c) <= ord('z')) | (ord('0') <= ord(c) <= ord('9'))):
            return True
        