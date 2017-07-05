from collections import defaultdict


class TrieNode(object):
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.word = ''
        self.isEnd = False


class Solution(object):
    def __init__(self):
        self.root = TrieNode()
        self.result = []

    def addWord(self, word):
        node = self.root
        for item in word:
            node = node.children[item]
        node.isEnd = True
        node.word = word

    def findAllConcatenatedWordsInADict(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        for word in words:
            if len(word):
                self.addWord(word)
        res = []
        for word in words:
            if self.dfs(word, 0, self.root, 0):
                res.append(word)
        return res

    def dfs(self, word, index, root, cnt):
        cur = root
        for i in range(index, len(word)):
            if not cur.children.get(word[i]):
                return False
            if cur.children.get(word[i]).isEnd:
                if i == len(word) - 1:
                    return cnt >= 1
                if self.dfs(word, i + 1, self.root, cnt + 1):
                    return True
            cur = cur.children.get(word[i])
        return False


class Solution(object):
    def findAllConcatenatedWordsInADict(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        word_set = set(words)
        res = []
        def helper(w, cur, cnt):
            if cur == len(w):
                if cnt > 1:
                    return True
                else:
                    return False
            for i in xrange(cur + 1, len(w) + 1):
                if w[cur:i] in word_set and helper(w, i, cnt + 1):
                    return True
            return False
        for w in words:
            if helper(w, 0, 0):
                res.append(w)
        return res
