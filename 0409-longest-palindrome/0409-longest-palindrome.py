class Solution:
    def longestPalindrome(self, s: str) -> int:
        dict = {}
        length = 0
        oddFound = False
        
        for char in s: 
            if char not in dict:
                dict[char] = 1
            else:
                dict[char] += 1
        
        for key, val in dict.items():
            if val % 2 == 0:
                length += val
            else:
                length += val - 1
                oddFound = True
        
        if oddFound:
            return length + 1
        else:
            return length
            