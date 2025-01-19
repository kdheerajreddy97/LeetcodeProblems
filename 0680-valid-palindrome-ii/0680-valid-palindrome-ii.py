# deleting not replacing
# try both the deletions
# Time: O(n); Space: O(n)
class Solution:
    def validPalindrome(self, s: str) -> bool:
        def checkpalindrome(l, r, s):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        i = 0
        j = len(s) - 1
        while i < j:
            if s[i] != s[j]:
                return checkpalindrome(i, j -1, s) or checkpalindrome(i + 1, j, s)
            i += 1
            j -= 1
        return True

            