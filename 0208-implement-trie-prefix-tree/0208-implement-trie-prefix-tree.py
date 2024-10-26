class Trie:
    
    class TrieNode:
        def __init__(self):
            self.isEnd = False
            self.children = [None] * 26
            
    def __init__(self):
        self.root = self.TrieNode()
        

    def insert(self, word: str) -> None:
        node = self.root
        for c in word:
            pos = ord(c) - ord('a')
            if not node.children[pos]:
                node.children[pos] = self.TrieNode()
            node = node.children[pos]
        node.isEnd = True


    def search(self, word: str) -> bool:
        node = self.root
        for c in word:
            pos = ord(c) - ord('a')
            if not node.children[pos]:
                return False
            node = node.children[pos]
        return node.isEnd
        

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for c in prefix:
            pos = ord(c) - ord('a')
            if not node.children[pos]:
                return False
            node = node.children[pos]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)