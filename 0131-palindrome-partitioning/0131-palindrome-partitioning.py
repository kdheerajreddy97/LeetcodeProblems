# More efficient than the below one as we are not creating a new list everytime
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        
        def helper(s, path):
            if not s:
                res.append(path[:])
                return
            
            for i in range(1,len(s)+1):
                partition = s[:i]
                if ispalindrome(partition):
                    #path = path + [partition]
                    path.append(partition)
                    helper(s[i:],path)
                    path.pop()
                

        
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
    
# class Solution:
#     def partition(self, s: str) -> List[List[str]]:
#         res = []
        
#         def helper(s, path):
#             if not s:
#                 res.append(path)
#                 return
            
#             for i in range(1, len(s) + 1):
#                 partition = s[:i]
#                 if is_palindrome(partition):
#                     helper(s[i:], path + [partition])
        
#         def is_palindrome(sub):
#             return sub == sub[::-1]  # Simple palindrome check
        
#         helper(s, [])
#         return res
