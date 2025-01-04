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
        for c in word[::-1]:  # Insert the reversed word
            pos = ord(c) - ord('a')
            if not node.children[pos]:
                node.children[pos] = TrieNode()
            node = node.children[pos]
        node.startsWith = True  # Mark the end of the word
    
class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = Trie()
        self.stream = []  # To store the stream of queried letters
        self.max_length = 0  # Keep track of the maximum word length
        
        # Insert all words into the Trie and track the maximum word length
        for word in words:
            self.trie.insert(word)
            self.max_length = max(self.max_length, len(word))

    def query(self, letter: str) -> bool:
        self.stream.append(letter)
        
        # Limit the stream size to the maximum word length for efficiency
        if len(self.stream) > self.max_length:
            self.stream.pop(0)

        # Start searching from the root of the Trie
        curr = self.trie.root
        for c in reversed(self.stream):  # Check prefixes in reverse order
            pos = ord(c) - ord('a')
            if not curr.children[pos]:
                return False
            curr = curr.children[pos]
            if curr.startsWith:
                return True  # Found a valid prefix
        return False


        


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)