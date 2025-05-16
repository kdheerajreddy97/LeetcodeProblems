# Dp - Memoization
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordset = set(wordDict)
        n = len(s)
        memo = set() # using memo set instead of hashmap
        def helper(sub):
            if len(sub) == 0:
                return True
            if sub in memo:
                return False

            for i in range(len(sub)):
                substr = sub[0: i+1]
                print(substr)
                if(substr in wordset) and (helper(sub[i+1:])):
                    return True

            memo.add(sub)
            return False

        return helper(s)