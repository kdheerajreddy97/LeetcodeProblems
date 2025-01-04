# Reverse the word and insert into the Trie
# Search for each prefix in this Trie
# Optimization: length of max word in stream
class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.startsWith = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root 
        for c in word[::-1]:
            pos = ord(c) - ord('a')
            if not node.children[pos]:
                node.children[pos] = TrieNode()
            node = node.children[pos]
        node.startsWith = True
    
class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = Trie()
        self.result = []
        self.max_length = 0
        for word in words:
            self.trie.insert(word)
            self.max_length = max(self.max_length, len(word))

    def query(self, letter: str) -> bool:
        curr = self.trie.root
        self.result.append(letter)
        if len(self.result) > self.max_length:
            self.result.pop(0)

        for c in self.result[::-1]:
            pos = ord(c) - ord('a')
            if not curr.children[pos]:
                return False
            curr = curr.children[pos]
            if curr.startsWith:
                return True
        return False

        


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)