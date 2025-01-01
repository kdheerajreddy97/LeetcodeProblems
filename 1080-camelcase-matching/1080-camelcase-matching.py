# Time: N O(m + n)
class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        res = []
        for query in queries:
            if self.matching(query, pattern):
                res.append(True)
            else:
                res.append(False)

        return res
    # 2 Pointers approach
    def matching(self, query, pattern):
        i = 0
        j = 0
        m = len(query)
        n = len(pattern)

        while j < n and i < m:
            if query[i] == pattern[j]:
                i += 1
                j += 1
            # No Match
            else:
                # If uppercase then return False - Ex: "FrameBuffeR"
                if query[i].isupper():
                    return False
                i += 1
        if i > m:
            return False
        if j == n and i <= m:
            # Check if the remaining string contains the UpperCase letters Ex: "FooBarTest"
            while i < m:
                if query[i].isupper():
                    return False
                i += 1
            return True

