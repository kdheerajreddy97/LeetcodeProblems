class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        dict1 = {}
        dict2 ={}
        
        n = len(s)

        for i in range(n):
            if s[i] in dict1 and dict1[s[i]] != t[i]:
                return False
            if t[i] in dict2 and dict2[t[i]] != s[i]:
                return False 
            dict1[s[i]] = t[i]
            dict2[t[i]] = s[i]
        return True

            


                
                
            
        
        
        
        
        