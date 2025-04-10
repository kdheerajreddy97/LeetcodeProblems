class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        countS = {}
        countP = {}
        res = []
        if len(s) < len(p):
            return []
        for i in range(len(p)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countP[p[i]] = 1 + countP.get(p[i], 0)

        if countS == countP: # O(26) - constant time
            res.append(0)
        l = 0
        for r in range(len(p), len(s)):
            countS[s[r]] = 1 + countS.get(s[r], 0)
            countS[s[l]] -= 1

            if countS[s[l]] == 0:
                del countS[s[l]]

            l += 1

            if countS == countP:
                res.append(l)
        return res



        

            
