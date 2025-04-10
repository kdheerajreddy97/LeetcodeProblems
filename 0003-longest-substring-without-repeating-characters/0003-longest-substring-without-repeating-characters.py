class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substr = set()
        n = len(s)
        if n == 0:
            return 0
        if n == 1:
            return 1
        l = 0
        r = 1
        max_length = 0
        substr.add(s[l])
        while r < n:
            if s[r] in substr:
                substr.remove(s[l])
                l += 1
            else:
                substr.add(s[r])
                
                max_length = max(max_length, r - l + 1)
                r += 1
            print(max_length)
        
        return max_length

            
            




