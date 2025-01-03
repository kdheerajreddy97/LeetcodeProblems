# Approach1: DFS with Recursion - Backtracking
# Approach2: Tries - DFS with Recursion - Backtracking
# Time: O(N * L) + O(N ^ L); Space: O(N * L) + O(N * L) [Tries + List]
class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.startsWith = []

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for c in word:
            pos = ord(c) - ord('a')
            if not node.children[pos]:
                node.children[pos] = TrieNode()
            node = node.children[pos]
            node.startsWith.append(word)
    
    def search(self, word):
        node = self.root
        for c in word:
            pos = ord(c) - ord('a')
            if not node.children[pos]:
                return []
            node = node.children[pos]
        return node.startsWith


class Solution:
    def __init__(self):
        self.result = []
        
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        trie = Trie()
        for word in words:
            trie.insert(word)

        path = []

        for word in words:
            # Action
            path.append(word)
            # Recurse
            self.dfs(path, words,trie)
            # Backtrack
            path.pop()
        return self.result

    def dfs(self, path, words,trie):
        # Base Case
        if len(path) == len(words[0]):
            self.result.append(path[:])
            return

        # Logic
        prefix = ""
        idx = len(path)
        for word in path:
            prefix += word[idx]
        
        startswithprefix = trie.search(prefix)

        for word in startswithprefix:
            # Action
            path.append(word)
            # Recurse
            self.dfs(path, words, trie)
            # Backtrack
            path.pop()

            

        
        

        
        
        