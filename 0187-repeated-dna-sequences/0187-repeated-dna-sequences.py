# Approach1: Brute Force approach: Linear- time slicing
# Approach2: Robin Karp's Rolling Hash Algorithmn

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        seen = set()
        res = set()
        n = len(s)
        for i in range(n-9):
            substr = s[i:i+10]
            if substr in seen:
                res.add(substr)
            seen.add(substr)
        return list(res)

        