class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substr = set()
        l = 0
        r = 0
        longest = 0
        
        for r in range(len(s)):
            while s[r] in substr:
                substr.remove(s[l])
                l+=1
            substr.add(s[r])
            longest = max(longest, r - l + 1)
        return longest
                
            