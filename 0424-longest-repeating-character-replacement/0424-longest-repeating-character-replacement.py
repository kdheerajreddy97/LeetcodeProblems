class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        dict = {}
        s = s.upper()
        l , r = 0 , 0
        longest = 0
        max_length = 0
        for r in range(len(s)):
            dict[s[r]] = dict.get(s[r], 0) + 1
            max_length = max(max_length, dict[s[r]])
            
            if (r-l+1)- max_length > k:
                dict[s[l]] -= 1
                l += 1
            
            longest = max(longest, r - l + 1)
            
        return longest