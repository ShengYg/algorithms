from collections import defaultdict

dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]


class TrieNode(object):
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.word = None


class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current = self.root
        for letter in word:
            current = current.children[letter]
        current.word = word


class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        tree = Trie()
        for word in words:
            tree.insert(word)
        current = tree.root
        n, m = len(board), len(board[0])
        board = [list(item) for item in board]
        res = []
        for i in range(n):
            for j in range(m):
                self.findsubword(board, i, j, current, res)
        return res

    def findsubword(self, board, i, j, current, res):
        c = board[i][j]
        if c in current.children:
            current = current.children.get(c)
            if current.word:
                res.append(current.word)
                current.word = None
            board[i][j] = '#'
            for this_dir in dirs:
                i1 = i + this_dir[0]
                j1 = j + this_dir[1]
                if 0 <= i1 < len(board) and 0 <= j1 < len(board[0]):
                    self.findsubword(board, i1, j1, current, res)
            board[i][j] = c
