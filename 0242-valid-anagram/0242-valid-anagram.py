class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq = {}
        if len(s)==len(t):
            for char in s:
                if char in freq:
                    freq[char] +=1
                else:
                    freq[char] =1

            for char in t:
                if char in freq:
                    freq[char] -=1
            print(freq)

            for value in freq.values():
                if value != 0:
                    return False
            return True
        else: 
            return False