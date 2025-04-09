class Solution:
    def customSortString(self, order: str, s: str) -> str:
        count = {}
        res = []
        for i in s:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1

        for c in order:
            while c in count:
                if count[c] > 0:
                    res.append(c)
                    count[c] -=1
                else:
                    break
        
        for j, freq in count.items():
            while freq > 0:
                res.append(j)
                freq -= 1
        return "".join(res)


