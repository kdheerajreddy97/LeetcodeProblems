class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s =s.split(" ")
        dict1 = {}
        dict2 = {}
        
        if len(pattern) != len(s):
            return False
        
        for i in range(len(pattern)):
            char = pattern[i]
            word = s[i]
            
            if ((char in dict1) and (dict1[char] != word)) or ((word in dict2) and (dict2[word] != char)):
                return False
            else:
                dict1[char] = word
                dict2[word] = char
        return True