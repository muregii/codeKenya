class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True
    
    def search_shortest_root(self, word):
        node = self.root
        root = ""
        for char in word:
            if char not in node.children:
                break
            node = node.children[char]
            root += char
            if node.is_end_of_word:
                return root
        return word

class Solution(object):
    def replaceWords(self, dictionary, sentence):
        """
        :type dictionary: List[str]
        :type sentence: str
        :rtype: str
        """
        trie = Trie()
        for root in dictionary:
            trie.insert(root)
        
        words = sentence.split()
        for i in range(len(words)):
            words[i] = trie.search_shortest_root(words[i])
        
        return " ".join(words)