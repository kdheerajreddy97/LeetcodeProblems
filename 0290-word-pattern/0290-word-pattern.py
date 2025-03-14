class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split(" ")
        dict1 = {}
        dict2 = {}
        if len(pattern) != len(s):
            return False

        for i in range(len(pattern)):
            p1 = pattern[i]
            s1 = s[i]
            if (p1 in dict1 and dict1[p1] != s1) or (s1 in dict2 and dict2[s1]!= p1):
                return False
            dict1[p1] = s1
            dict2[s1] = p1
        return True
