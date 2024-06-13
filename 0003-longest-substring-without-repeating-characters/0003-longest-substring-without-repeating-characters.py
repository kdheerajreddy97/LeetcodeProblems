class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        substr = set()
        max_length = 0
        for r, char in enumerate(s):
            while char in substr:
                substr.remove(s[l])
                l = l + 1
                
            substr.add(char)
            max_length = max(max_length, r - l + 1)
        return max_length
            
            
                