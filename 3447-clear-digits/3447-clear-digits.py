class Solution:
    def clearDigits(self, s: str) -> str:
        n = len(s)
        i = 0
        res = []
        while i < n:
            if s[i].isalpha():
                res.append(s[i])
                i += 1
            else:
                if len(res) >= 1:
                    res.pop(-1)
                i += 1
        return "".join(res)
                


        