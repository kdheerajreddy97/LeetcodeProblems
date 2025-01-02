# Approach: Consecutive elemeents comparision and use dicitionary to store the postions of order
# Time: O(N*L); Space: O(1)
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        dict = {}
        for i, c in enumerate(order):
            dict[c] = i
        for i in range(len(words)-1):
            # Check if not ordered
            if not self.isordered(words[i], words[i+1],dict):
                return False
        return True

    def isordered(self, word1, word2, dict):
        minimum = min(len(word1), len(word2))
        for i in range(minimum):
            # check if it is breaking i.e. not lexographical
            if dict[word1[i]] > dict[word2[i]] :
                return False
            # If it is lexographical at this position return True
            elif dict[word1[i]] < dict[word2[i]]:
                return True
        # Most imp if two words of same characters but one words contains extra characters
        return len(word1) <= len(word2)
            
                          