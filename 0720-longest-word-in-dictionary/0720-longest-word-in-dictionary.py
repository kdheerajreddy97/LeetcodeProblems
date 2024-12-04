# When to use tries: To find prefixes
class TrieNode:
    def __init__(self):
        self.isEnd = False
        self.children = [None] * 26

class Solution:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self,word):
        node = self.root
        for c in word:
            pos = ord(c) - ord('a')
            if not node.children[pos]:
                node.children[pos] = TrieNode()
            node = node.children[pos]
        node.isEnd = True
    
    
    def search(self, word):
        node = self.root
        for c in word:
            pos = ord(c) - ord('a')
            node = node.children[pos]
            if not node or not node.isEnd:
                return False
        return True
                
            
    
    def longestWord(self, words: List[str]) -> str:
        
        # Building the prefix trie
        for word in words:
            self.insert(word)
            
        # Sort the words by length and lexicographical order
        words.sort(key=lambda x: (-len(x), x))
        
        # Check if all the prefixes for that word are present in the list
        for word in words:
            if self.search(word):
                return word
            
        return ""
                
                
            
    
        
        
        
        
        
        