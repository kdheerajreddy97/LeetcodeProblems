# DFS with backtracking
# Time: O(k^m); Space: O(k^m)
class Solution:
    def parse(self, s):
        # Parsing the given string to List[Lists]
        res = []
        n = len(s)
        i = 0
        while i < len(s):
            temp_list = []
            if s[i] == "{":
                i += 1
                while s[i] != "}" and i < n-1:
                    if s[i] == ",":
                        i += 1
                    else:
                        temp_list.append(s[i])
                        i += 1
                i += 1
                # Make sure to sort
                res.append(sorted(temp_list))
            else:
                res.append([s[i]])
                i += 1
        return res
    

    # DFS + Backtracking to get the list of all possible strings
    def dfs(self, i, path, options, result):
        # Basecase
        if i == len(options):
            result.append("".join(path))
            return

        for option in options[i]:
            path.append(option)
            # Recurse
            self.dfs(i+1, path, options, result)
            # Backtrack
            path.pop()

    # Main function to call the parse(s) and pass the resulting array to dfs for backtrack
    def expand(self, s: str) -> List[str]:
        options = self.parse(s)
        result = []
        # Variables to pass - index, path to build and backtrack, option, result
        self.dfs(0, [], options , result)
        return result


        
        

                        
                    


        