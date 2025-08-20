# Word Search II LeetCode Challenge
# Given a 2-D grid of characters board and a list of strings words, return all words that are present in the grid.
# For a word to be present it must be possible to form the word with a path in the board with horizontally or vertically neighboring cells. 
# The same cell may not be used more than once in a word.
class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None

def find_words(board, words):
    root = TrieNode()
    for w in words:
        node = root
        for c in w:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.word = w

    rows, cols = len(board), len(board[0])
    res, visited = set(), set()

    def dfs(r, c, node):
        if (r < 0 or c < 0 or r >= rows or c >= cols or 
            (r, c) in visited or board[r][c] not in node.children):
            return
        visited.add((r, c))
        node = node.children[board[r][c]]
        if node.word:
            res.add(node.word)
        dfs(r+1, c, node)
        dfs(r-1, c, node)
        dfs(r, c+1, node)
        dfs(r, c-1, node)
        visited.remove((r, c))

    for r in range(rows):
        for c in range(cols):
            dfs(r, c, root)

    return list(res)

# TestCase
board = [
  ["a","b","c","d"],
  ["s","a","a","t"],
  ["a","c","k","e"],
  ["a","c","d","n"]
]
words = ["bat","cat","back","backend","stack"]
print(find_words(board, words))

# Time Complexity: O(m * n * 4^L) where L = max word length
# Space Complexity: O(k * L) where k = number of words
