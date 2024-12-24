# Approach1: Brute Force approach: Linear- time slicing
# Approach2: Robin Karp's Rolling Hash Algorithmn
# Time: O((N-L)L); Space: O((N-L)L)
# class Solution:
#     def findRepeatedDnaSequences(self, s: str) -> List[str]:
        # seen = set()
        # res = set()
        # n = len(s)
        # for i in range(n-9):
        #     substr = s[i:i+10]
        #     if substr in seen:
        #         res.add(substr)
        #     seen.add(substr)
        # return list(res)
# Time: O(N-L); Space: O(N-L)
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:    
        # Rolling has parameters
        a = 4
        l = 10
        var = pow(a,l)
        h = 0
        n = len(s)  
        seen = set()
        output = set()
        # Converting string to array of integers
        nums = [] * n
        DNA = {"A": 0, "C": 1, "G": 2, "T": 3}
        for i in range(n):
            nums.append(DNA.get(s[i]))

        for start in range(n-l+1):
            # Compute the hash value
            if start == 0:
                for i in range(l):
                    h = h * a + nums[i]
            else:
                h = h * a - nums[start - 1] * var + nums[start + l - 1]
            # update output and hashset of seen sequences
            if h in seen:
                output.add(s[start: start + l])
            seen.add(h)

        return list(output)
        

