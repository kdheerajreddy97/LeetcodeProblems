class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        
        def helper(s, path):
            if not s:
                res.append(path)
                return
            
            for i in range(1,len(s)+1):
                partition = s[:i]
                if ispalindrome(partition):
                    helper(s[i:],path + [partition])
                

        
        def ispalindrome(path):
            l = 0
            r = len(path) -1
            while l < r:
                if path[l] != path[r]:
                    return False
                l += 1
                r -= 1
            return True
        
        helper(s, [])
        return res