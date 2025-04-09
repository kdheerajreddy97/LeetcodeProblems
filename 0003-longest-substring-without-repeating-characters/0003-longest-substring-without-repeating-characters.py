#Any approach works: Binary search, Two pointers, Hashing, Sliding Window works
# Two pointers and Sliding window are more optimized
# time complexity: O(n)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
#         l = 0
#         substr = set()
#         max_length = 0
#         for r, char in enumerate(s):
#             while char in substr:
#                 substr.remove(s[l])
#                 l = l + 1
                
#             substr.add(char)
#             max_length = max(max_length, r - l + 1)
#         return max_length
            
        substr = set()
        n = len(s)
        if n == 1:
            return 1
        if n == 0:
            return 0
        l = 0
        r = 1
        longest = 0
        substr.add(s[l]) #O(1) only 26 max size
        while (r <= n-1):
            if s[r] in substr:
                substr.remove(s[l])
                l += 1
            else:
                substr.add(s[r])
                r += 1
                longest = max(longest, r-l)
        return longest
                
            
                