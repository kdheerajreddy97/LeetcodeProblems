#Brute force way takes O(n!) time complexity as we need to generate all the possible permutation of source string
#More optimized way woud be this with O(n) time complexity
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        count = {}
        res = ""
        for i in s: 
            if i in count:
                count[i] += 1
            else:
                count[i] = 1
                
        for j in order:
            while j in count:
                if count[j] != 0:
                    count[j] -= 1
                    res += j  
                else:
                    break
                
        for key,val in count.items():
            while val != 0:
                res += key
                val -= 1
                
        
        return res
            
                