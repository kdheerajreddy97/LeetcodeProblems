class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        char_set = set()
        max_length = 0
        
        while r < len(s):
            if s[r] in char_set:
                char_set.remove(s[l])
                l +=1
            else:
                char_set.add(s[r])
                max_length = max(max_length, r - l + 1)
                r = r + 1
        return max_length