class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        List_S = list(s)

        for i in sorted(range(len(indices)), key = lambda k:indices[k], reverse = True):
            x = indices[i]
            y = sources[i]
            z = targets[i]
            match = True
            for j in range(len(y)):
                if x + j >= len(s) or s[x + j] != y[j]:
                    match = False
                    break
            if match:
                List_S[x:x+len(y)] = list(z)

        return "".join(List_S)
                





        # k = len(indices)
        # dict = defaultdict(list)
        # for i in range(k):
        #     substr2 = sources[i]
        #     index = indices[i]
        #     index2 = index + len(substr2)
        #     substr1 = s[index:index2]
        #     if substr1 == substr2:
        #         dict[index].append(targets[i])
            
        # for key, values in dict.items():
        #     for val in values:
        #         if key == 0:
        #             s = val + s[key+1:]
        #         else:
        #             s = s[:key] + val + s[key+1:]
        #     print(s)
        # return s


