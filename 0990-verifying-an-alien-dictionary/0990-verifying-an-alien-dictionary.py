class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        
        dict = {}

        for i, c in enumerate(order):
            dict[c] = i
        
        for i in range(len(words)-1):
            if not self.isordered(words[i], words[i+1],dict):
                return False

        return True

    def isordered(self, word1, word2, dict):
        print(word1)
        print(word2)
        minimum = min(len(word1), len(word2))
        for i in range(minimum):
            if dict[word1[i]] > dict[word2[i]] :
                print(i)
                print(dict[word1[i]])
                print(dict[word2[i]])
                return False
            elif dict[word1[i]] < dict[word2[i]]:
                return True
        return len(word1) <= len(word2)
            
                          