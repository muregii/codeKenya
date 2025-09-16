# Design Add and Search Word Data Structure Leetcode Challenge
# Design a data structure that supports adding new words and searching for existing words.
# Implement the WordDictionary class:
# void addWord(word) Adds word to the data structure.
# bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. 
# word may contain dots '.' where dots can be matched with any letter.

class WordDictionary:
    def __init__(self):
        self.root = {}

    def add_word(self, word):
        node = self.root
        for c in word:
            if c not in node:
                node[c] = {}
            node = node[c]
        node["$"] = True

    def search(self, word):
        def dfs(j, node):
            for i in range(j, len(word)):
                c = word[i]
                if c == ".":
                    for child in node:
                        if child != "$" and dfs(i+1, node[child]):
                            return True
                    return False
                else:
                    if c not in node:
                        return False
                    node = node[c]
            return "$" in node
        return dfs(0, self.root)

# usage
wd = WordDictionary()
wd.add_word("bad")
wd.add_word("dad")
wd.add_word("mad")
print(wd.search("pad"))
print(wd.search("bad"))  
print(wd.search(".ad"))  

# Time Complexity: O(n) for add, O(n) worst case for search
# Space Complexity: O(n * k) where k = number of words
