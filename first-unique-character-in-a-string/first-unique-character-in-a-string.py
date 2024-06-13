class Solution:
    def firstUniqChar(self, s: str) -> int:
        my_dict = {}
        
        for letter in s:
            if letter in my_dict:
                my_dict[letter] += 1
            else:
                my_dict[letter] = 1
        
        
        for index in range(len(s)):
            if my_dict[s[index]] == 1:
                return index
        return -1
            
            
                
            
        