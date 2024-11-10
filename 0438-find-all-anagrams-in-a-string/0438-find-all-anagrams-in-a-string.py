# Worst Brute Force: n! *(m*n) - Generate and compare all the subsrtings
# Better Brute Force: Form all the strings of length p. Then use any of these techniques
# 1. Sort - nlog(n)
# 2. Prime Product - (m-n) * n
# 3. Frequency - (m-n) * n

#Sliding window O(m + n)
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        l = 0
        countS = {}
        countP = {}
        res = []
        
        if len(s) < len(p): 
            return []
        
        for i in range(len(p)):
            countP[p[i]] = 1 + countP.get(p[i],0)
            countS[s[i]] = 1 + countS.get(s[i],0)
        
        if countP == countS:
            res = [0]
        else:
            res = []
        for r in range(len(p), len(s)):
            countS[s[r]] = 1 + countS.get(s[r],0)
            countS[s[l]] = countS[s[l]] - 1
            
            if countS[s[l]] == 0:
                del countS[s[l]]
            
            l = l + 1
            if countS == countP:
                res.append(l)
        
        return res
            