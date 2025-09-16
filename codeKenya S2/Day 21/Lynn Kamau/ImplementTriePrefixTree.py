# Implement Trie (Prefix Tree) Leetcode Challenge
# A prefix tree (also known as a trie) is a tree data structure used to efficiently store and retrieve keys in a set of strings. Some applications of this data structure include auto-complete and spell checker systems.
# Implement the PrefixTree class:
# PrefixTree() Initializes the prefix tree object.
# void insert(String word) Inserts the string word into the prefix tree.
# boolean search(String word) Returns true if the string word is in the prefix tree (i.e., was inserted before), and false otherwise.
# boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.

class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.end = True

    def search(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                return False
            node = node.children[c]
        return node.end

    def starts_with(self, prefix):
        node = self.root
        for c in prefix:
            if c not in node.children:
                return False
            node = node.children[c]
        return True

# Test Case
trie = Trie()
trie.insert("apple")
print(trie.search("apple"))  
print(trie.search("app"))     
print(trie.starts_with("app"))

# Time Complexity: O(n) per word (n = length of word)
# Space Complexity: O(n * k) where k = number of words
