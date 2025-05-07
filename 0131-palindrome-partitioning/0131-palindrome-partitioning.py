class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        n = len(s)

        def helper(path, pivot):
            if pivot == n:
                res.append(path[:])
                return

            for i in range(pivot, n):
                partition = s[pivot:i+1]
                if partition == partition[::-1]:
                    path.append(partition)
                    helper(path,i+1)
                    path.pop()

        helper([],0)
        return res