class Solution:
    def parse(self, s):
        n = len(s)
        res = []
        i = 0
        while i < n:
            templist = []
            if s[i] == "{":
                i += 1
                templist.append(s[i])
                i += 1
                while s[i] != "}":
                    if s[i] == ",":
                        i += 1
                    else:
                        templist.append(s[i])
                        i += 1
                i += 1
            else:
                templist.append(s[i])
                i += 1
            res.append(sorted(templist))
        return res



    def expand(self, s: str) -> List[str]:
        res = []
        options = self.parse(s)

        def helper(path, pivot):
            if pivot == len(options):
                res.append("".join(path))
                return

            for option in options[pivot]:
                path.append(option)
                helper(path, pivot + 1)
                path.pop()

        helper([],0)
        return res



        