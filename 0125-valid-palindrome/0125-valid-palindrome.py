class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = ""
        rev =""
        for char in s:
            if char.isalnum():
                res += char
        res = res.lower()
        rev = res[::-1]
        return (res == rev)
        