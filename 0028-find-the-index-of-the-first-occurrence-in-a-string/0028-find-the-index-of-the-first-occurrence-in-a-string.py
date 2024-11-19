#Brute way - O(m*n) time complexity
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        for i in range(len(haystack)):
            k = i
            j = 0
            while j < len(needle) and k < len(haystack) and haystack[k] == needle[j]:
                k += 1
                j += 1
            if j == len(needle):
                return i
            
        return -1
                
                
                
                    
                
        
        